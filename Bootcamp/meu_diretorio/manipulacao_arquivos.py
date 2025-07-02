# 1. Introdução à manipulação de arquivos
arquivo = open("exemplo.txt", "w")
arquivo.write("Bem-vindo ao mundo da manipulacao de arquivos!")
arquivo.close()

# 2. Abrindo e fechando arquivos
arquivo = open("exemplo.txt", "r")
conteudo = arquivo.read()
print("Conteúdo do arquivo:", conteudo)
arquivo.close()

# 3. Lendo de um arquivo
arquivo = open("exemplo.txt", "r")
linhas = arquivo.readlines()
for linha in linhas:
    print("Linha lida:", linha.strip())
arquivo.close()

# 4. Escrevendo em um arquivo
arquivo = open("dados.txt", "w")
arquivo.write("Primeira linha do arquivo.\n")
arquivo.writelines(["Segunda linha.\n", "Terceira linha.\n"])
arquivo.close()

# 5. Gerenciando arquivos e diretórios
import os
if os.path.exists("dados.txt"):
    print("Arquivo encontrado!")
os.rename("dados.txt", "dados_renomeado.txt")
os.remove("dados_renomeado.txt")
os.mkdir("meu_diretorio")
print("Arquivos:", os.listdir("."))

# 6. Tratamento de exceções em manipulação de arquivos
try:
    arquivo = open("inexistente.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
finally:
    try:
        arquivo.close()
    except:
        pass

# 7. Boas práticas na manipulação de arquivos
with open("boas_praticas.txt", "w") as arquivo:
    arquivo.write("Arquivo manipulado com boas práticas.\n")
    arquivo.write("Não é necessário chamar close().")

with open("boas_praticas.txt", "r") as arquivo:
    for linha in arquivo:
        print("Linha:", linha.strip())
