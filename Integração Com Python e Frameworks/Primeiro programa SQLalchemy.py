#Para trabalhar com criação de tabelas e banco de dados em python devemos importar boa parte dos atributos que iremos usar para trabalhar
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import session
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import func

#Uma classe que usamos para criar uma tabela, fazemos que as classes que iremos trabalhar herdem este atributo declarative_base()
Base = declarative_base()


class User(Base):
    #Devemos sempre definir um nome para nossa tabela
    __tablename__ = "User_account"
    #Criação da tabela, devemos estipular seus atributos, como por exemplo tipo de valor, coluna, entre algumas regras da coluna
    id = Column(Integer, primary_key = True)
    name = Column(String)
    fullname = Column(String)


    #Forma de relacionamento entre tabelas, onde utilizamos valores de uma outra tabela para sua tabela principal
    address = relationship(
        "Address", back_populates = "user", cascade = "all, delete-orphan"
    ) 

    def __repr__(self):
        return f"User(id = {self.id}, name = {self.name}, fullname = {self.fullname} address = {self.address})"

class Address(Base):
    __tablename__ = "User_address"
    id = Column(Integer, primary_key = True, autoincrement = True)
    email_address = Column(String(30), nullable = False)
    user_id = Column(Integer, ForeignKey("User_account.id"), nullable = False)  

    user = relationship("User", back_populates = "address")

    def __repr__(self):
        return f"Address(id = {self.id}, email_address = {self.email_address}, user = {self.user})"
    

tabela = User()
print(tabela,"\n")
endereco = Address()
print(endereco,"\n")

#Conexão com Banco de Dados
engine = create_engine('sqlite://')

#Criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)
 
#Definimos um inspect para acessar o banco de dados
inspetor_engine = inspect(engine)
#Retorna o nome das tabelas criadas
print(inspetor_engine.get_table_names(),"\n")
#Retorna se existe uma tabela com o nome definido no metodo
print(inspetor_engine.has_table("User_account"),"\n")
#Retorna o nome do banco de dados 
print(inspetor_engine.default_schema_name,"\n")

#Definindo os valores para inserir no BD
with Session(engine) as session:
    #Definimos a tabela que será inserida os valores, e então usamos os nomes das colunas que definimos lá em cima recebendo os valores
    User_1 = User(
        id = 1,
        name =  "gustavo",
        fullname = "gustavo henrique", 
        #Neste caso o valor é preenchido em outra tabela, acessando a coluna da tabela chamando a sua Classe
        address = [Address(email_address = 'gustavo1234@email.com')]
    )

    User_2 = User(
        id = 2,
        name = "henrique",
        fullname = "henrique alfredo",
        address = [Address(email_address = 'henrique1234@gmail.com')]
    )

#Enviando os dados para o BD
session.add_all([User_1, User_2])
#Commit é usado para confirmar as alterações ou criação de valores no banco de dados
session.commit()

#Forma para exibir os valores da tabela
#Select é usado para recuperar informações, usamos o Select e em seguida a tabela que iremos acessar seus valores
stmt = select(User).where(User.name.in_(['henrique']))
for user in session.scalars(stmt):
    print(user,"\n")

#Forma para exibir os valores da tabela, buscando por um valor específico 
stmt_address = select(Address).where(Address.user_id.in_([1])) 
for address in session.scalars(stmt_address):
    print(address,"\n")

#Forma de exibir os valores da tabela buscando por ordem, podendo ser crescente e decrescente
stmt_order = select(User).order_by(User.fullname.desc())
for result in session.scalars(stmt_order):
    print(result,"\n")

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
#Scalars não consegue retornar os valores selecionados de duas tabelas, usamos outra maneira de trabalhar com duas tabelas
for join in session.scalars(stmt_join):
    print(join,"\n")


connect = engine.connect()
#Com o fetchall conseguimos recuperar os valores de duas tabelas usando o join 
results = connect.execute(stmt_join).fetchall()
for value in results:
    print(value,"\n")

#A função count conta o total instâncias, em uma tabela especifíca  
stmt_count = select(func.count('*')).select_from(User)
for count in session.scalars(stmt_count):
    print(count,"\n")


