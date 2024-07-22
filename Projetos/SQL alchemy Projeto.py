from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import BINARY
from sqlalchemy import DECIMAL
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo as pyM


Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String)

    contas = relationship("Conta", back_populates = "cliente")

class Conta(Base):
    __tablename__ = "conta"
    
    id = Column(Integer, primary_key = True)
    tipo = Column(String)
    agencia = Column(String)
    numero = Column(Integer)
    saldo = Column(DECIMAL)
    id_cliente = Column(Integer, ForeignKey('cliente.id'))

    cliente = relationship("Cliente", back_populates = "contas")

# Criação do motor de banco de dados
engine = create_engine('sqlite:///banco_de_dados.db')
Base.metadata.create_all(engine)

# Criação de uma sessão
Session = sessionmaker(bind = engine)
session = Session()

# Inserção de um conjunto de dados mínimo
cliente1 = Cliente(
    nome = "Gustavo Henrique",
    cpf = "123456789",
    endereco = "Americana"
)

conta1 = Conta(
    tipo = "Corrente",
    agencia = "1234",
    numero = 1,
    saldo = 1000,
    cliente = cliente1
)

# Adicionando os objetos na sessão
session.add(cliente1)
session.add(conta1)

# Commit da sessão para salvar no banco de dados
session.commit()

# Recuperação de dados
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(f"Cliente: {cliente.nome}, CPF: {cliente.cpf}, Endereço: {cliente.endereco}")
    print()
    for conta in cliente.contas:
        print(f"  Conta: {conta.tipo}, Agência: {conta.agencia}, Número: {conta.numero}, Saldo: {conta.saldo}")
        print()

session.close()


# PyMongo
client = pyM.MongoClient("mongodb+srv://gustavohe1412:aaa12311@cluster0.uddxwvd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Criação do banco de dados e da coleção
db = client['meu_banco']
colecao_clientes = db['clientes']

# Estrutura do documento de cliente
cliente_documento = {
    "nome": "Gustavo Henrique",
    "cpf": "123456789",
    "endereco": "Americana",
    "contas": [
        {
            "tipo": "Corrente",
            "agencia": "1234",
            "numero": 1,
            "saldo": 1000
        }
    ]
}

# Inserindo o documento na coleção
colecao_clientes.insert_one(cliente_documento)

# Recuperação de informações
clientes = colecao_clientes.find()
for cliente in clientes:
    print(f"Cliente: {cliente['nome']}, CPF: {cliente['cpf']}, Endereço: {cliente['endereco']}")
    print()
    for conta in cliente['contas']:
        print(f"  Conta: {conta['tipo']}, Agência: {conta['agencia']}, Número: {conta['numero']}, Saldo: {conta['saldo']}")
        print()