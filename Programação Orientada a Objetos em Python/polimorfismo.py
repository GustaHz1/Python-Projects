 #POLIMORFISMO consiste em uma CLASSE FILHA que possui o mesmo METODO da CLASSE PAI não deseja usar o METODO da mesma maneira que a PAI
#CLASSE PAI
class Animal:
    def andar(self):
        print("Andando...")

#CLASSE HERDEIRA
#Em casos que a CLASSE não possua seu prórpio METODO a FUNÇÃO a ser executada será a da CLASSE PAI
class Vaca(Animal):
    def andar(self):
        super().andar()

#CLASSE HERDEIRA
class Cobra(Animal):
    def andar(self):
        print("Rastejando...")

#CLASSE HERDEIRA
class Canguru(Animal):
    def andar(self):
        print("Pulando...")


#METODO que realizar a execução dos METODOS das CLASSES
def forma_andar(obj):
    obj.andar()


#Variaveis recebendo as CLASSES
f1 = Vaca()
f2 = Cobra()
f3 = Canguru()

#METODO recebendo as CLASSES por meio de uma variavel 
#Também pode passar as CLASSES direto no METODO sem precisar usar variaveis 
forma_andar(f1)
forma_andar(f2)
forma_andar(f3)