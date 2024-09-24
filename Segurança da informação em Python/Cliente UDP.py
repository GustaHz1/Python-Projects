import socket

# Criando o objeto de conexão
conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente Socket criado com sucesso! ")

host = "local_host"
porta = 5432
mensagem = input("Digite a mensagem que deseja enviar: ")

try:
    # Enviando a mensagem do Usuário para o servidor
    print(F"Cliente: {mensagem}")
    conexao.sendto(mensagem.encode(), (host, 5432))

    # Recebendo uma respota do servidor e desempacotar a mensagem
    dados = conexao.recvfrom(4096)
    servidor = conexao.recvfrom(4096)
    dados = dados.decode()
    print(f"Cliente {dados}")

finally:
    print("Cliente: Fechando a conexão! ")
    conexao.close()