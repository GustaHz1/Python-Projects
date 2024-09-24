import socket
import sys

def main():
    try:
        conexão = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    
    except socket.error as e:
        print("A conexão falhou!!")
        print(f"Eroo: {e}")
        sys.exit()

    print("Socket criado com sucesso!")

    host_alvo = input("Digite o Host ou IP a ser conectado: ")
    porta_alvo = int(input("Digite a Porta a ser conectada: "))

    try:
        conexão.connect((host_alvo, porta_alvo))
        print(f"Cliente TCP conectado com sucesso no Host {host_alvo} e na porta alvo {porta_alvo}")
        conexão.shutdown(2)

    except socket.error as e:
        print(f"Não foi possivel conectar no Host: {host_alvo} e na porta alvo {porta_alvo}")
        print(f"Erro: {e}")
        sys.exit()


if __name__ == "__main__":
    main()
