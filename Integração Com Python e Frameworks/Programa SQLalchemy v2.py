from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import text


#Forma alternativa para criar uma tabela 
engine = create_engine('sqlite://')

metadata_obj = MetaData()
user = Table(
    'user',
    metadata_obj,
    Column('Name', String(40), primary_key = True),
    Column('Telephone', Integer, nullable = False),
    Column('Email', String(30), nullable = False),
    Column('Address', String(50), nullable = False)
)
#Inserindo informações na tabela user
sql_insert = text("insert into user values('Gustavo', 19982602082, 'gustavo1234@gail.com', 'Americana Sp')")

user_data = Table(
    'user_data',
    metadata_obj,
    Column('name', String(40), ForeignKey('user.Name'), nullable = False),
    Column('Cpf', Integer, primary_key = True, nullable = False),
    Column('Rg', Integer, nullable = False),
)

#Sorted_tables busca as tabelas criadas por ordem
for table in metadata_obj.sorted_tables:
    print(table)


metadata__bd_obj = MetaData()
user_account = Table(
    'user_account',
    metadata__bd_obj,
    Column('cpf', Integer,  ForeignKey('user_data.Cpf'), nullable = False),
    Column('Account', Integer, primary_key = True, nullable = False),
    Column('Type_account', String(20), nullable = False),
)

#Usamos o nome da tabela em seguida um valor ou uma definição da tabela que queremos visualizar
print(user_account.primary_key,"\n")
print(user_account.foreign_keys,"\n")

metadata_obj.create_all(engine)

