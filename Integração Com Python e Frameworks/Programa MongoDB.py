import pymongo as pyM
import pprint

#Definindo a conexão com o Mongodb
client = pyM.MongoClient("mongodb+srv://gustavohe1412:aaa12311@cluster0.uddxwvd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

#Criando o Banco de dados
db = client.test
collection = db.test_collection
print(db.test_collection,"\n")

#Submeter as informações
posts = db.posts

#Definição de informação para compor o documento 
post = [{
    "author": "Gustavo",
    "text": "I learning Pymongo",
    "tags": ["mongodb", "python", "pymongo"]
}]

#Metodo para exibir o nome dos documentos
print(db.list_collection_names(),"\n")
#Metodo para exibir um documento
print(db.posts.find_one(),"\n")


new_post = [{
    "author": "Henrique",
    "text": "I learning Python",
    "tags": ["Python", "Coding"]},
    {
    "author": "Alfredo",
    "text": "I reading a book código limpo",
    "tags": ["Reading", "Java"]
}]

#O If tem como função impedir que este trecho do código seja executada sempre, assim evitando que em cada execução do código um novo documento seja adicionado
executar = input("Deseja executar este bloco do código (Caso sejá executado o código ira inserir diversos documentos) [S]Sim [N]Não ")
print()

if executar == 'S':
    #Sempre se atentar ao inserir documentos ao BD, pois toda vez que o código é executado um novo documento é adicionado 
    #Inserindo vários documentos ao BD
    posts.insert_many(post)
    result = posts.insert_many(new_post)
    #Inserindo vários IDS
    print(result.inserted_ids,"\n")

elif executar == 'N':
    pass

else:
    print("Valor incorreto! ")


#Recuperando um documento passando um valor específico para a busca
print(db.posts.find_one({"author":"Alfredo"}),"\n")

#Função usada para contar o total de documentos criados em nosso BD
print(posts.count_documents({}))
#Também podemos usar está função passando valores específicos para a busca
print(posts.count_documents({"author":"Gustavo"}))

for post in posts.find({}).sort("tags"):
    pprint.pprint(post)


user_profile = [
    {'user_id' : 1, 'name' : 'Bianca'},
    {'user_id' : 2, 'name' : 'Maria'}
]

#O If impede que este trecho código seja executado sempre, evitando a criação de vários documentos iguais no BD  
executar = input("Deseja executar este bloco do código (Caso sejá executado o código ira inserir diversos documentos) [S]Sim [N]Não ")
print()
    
if executar == 'S':
    inserir = db.user_profile.insert_many(user_profile)

elif executar == 'N':
    pass

else:
    print("Valor incorreto!")

#Exibir as coleções no BD
collections = db.list_collection_names()
for collection in collections:
    pprint.pprint(collection)
    print()

#A Função drop é utiliza para remover os documentos criados no DB
deletar = input("Deseja deletar os documentos criados: [S]Sim [N]Não \n")

if deletar == 'S':
    #Delete é um metedo que podemos chamar e passar valores específicos para ser deletado 
    posts.delete_one({"author" : "Alfredo"})
    #Drop deletamos tudo sem passar valores específicos 
    db.drop_collection(posts)
 
elif deletar == 'N':
    pass

else:
    print("Valor incorreto! ")


#A função drop_database deleta o BD com todas as informações que inserirmos, chamamos a variavel que recebe o servidos, em seguida o nome do BD e por fim a função
deletar_bd = input("Deseja deletar o banco de dados [S]Sim [N]Não ")

if deletar_bd == 'S':
    client.drop_database('test')

elif deletar_bd == 'N':
    pass

else:
    print("Valor incorreto! ")
