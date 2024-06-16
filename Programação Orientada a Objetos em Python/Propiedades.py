class Foo:
    def __init__(self, x):
        self._x = x

    #Property é usado para exibir o valor do METODO
    @property
    def x(self):
        return self._x or 0 
    
    #SETTER mais o nome do METODO é utilizado para modificar trabalhar com os valores do METODO
    @x.setter
    def x(self, value):
        self._x += value

foo = Foo(10)
print(foo.x)
#Este comando faz com que o valor selecionado seja somado a variavel
foo.x = 10
print(foo.x,"\n")


class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    #Propriedade para retornar a variavel nome
    @property
    def nome(self):
        return self._nome
    

    @property
    def idade(self):
        #Definimos uma variavel com valor fixo
        _ano_atual = 2024
        #O return ira voltar o resultado da operação 
        return _ano_atual - self._ano_nascimento
    


pessoa = Pessoa("Gustavo", 2005)
#Formatação para exibir os valores, \T é usado para dar um espaço 
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")