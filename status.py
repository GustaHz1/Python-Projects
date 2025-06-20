n = 0
projetos = []
status = []

while n < 3:
    projeto = input("Digite o nome do projeto: ")
    statu = input("Digite o status do projeto: ")
    projetos.append(projeto)
    status.append(statu)
    n +=1
    
for item, processo in zip(projetos, status):
    print(f"{item} = {processo}")    
    