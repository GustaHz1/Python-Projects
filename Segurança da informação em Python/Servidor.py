import socket

conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com Sucesso!")

host = "local_host"
port = 5432

conexao.bind((host, port))
mensagem = "Servidor: Cliente conectado"

while 1:
    dados = conexao.recvfrom(4096)
    if dados:
        print("Servidor enviando mensagem...")
        conexao.sendto(dados, (mensagem.encode()))