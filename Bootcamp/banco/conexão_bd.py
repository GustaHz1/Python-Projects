import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Criando um banco de dados com sqlite
conexao = sqlite3.connect(ROOT_PATH / "clientes.sqlite")
# Salvar o cursor
cursor = conexao.cursor()

# Criando uma tabela no banco e passando suas colunas e tipos
def criar_tabela(cursor):
    # Após execuatar uma vez não devemos executar a linha de criar uma tabela novamente
    cursor.execute("CREATE TABLE clientes (id INTENGER PRIMARY KEY, nome VARCHAR(100), email VARCHAR(150))")
    
def inserir_registro(conexao, cursor, nome, email):
    dados = (nome, email)    
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", dados)
    # Sempre dar commit quando inserir valores 
    conexao.commit()
    
def atualizar(conexao, cursor, id, nome):
    data = (id, nome)
    # Atualizando o id quando o valor da coluna campo for igual ao passado na função 
    cursor.execute('UPDATE clientes SET id=? WHERE nome=?;', data)
    conexao.commit()
    
def recuperar_cliente(cursor, id):
    # Função para retornar valores da tabela
    cursor.execute("SELECT * FROM clientes WHERE id=?;", (id,))
    return cursor.fetchone()

def listar_clientes(cursos):
    #Exibindo a tabela com ordenação de dados
    return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")

cliente = recuperar_cliente(cursor, 1)
print(cliente)

exibir = listar_clientes(cursor)
for user in exibir:
    print(user)

"""inserir_registro(conexao, cursor, "Henrique", "henrique@gmail.com")
atualizar(conexao, cursor, 2, "Henrique")"""