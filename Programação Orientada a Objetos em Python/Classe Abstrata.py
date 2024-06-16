#Para trabalhar com Classes Abstratas devemos importar a CLASSE ABC
from abc import ABC, abstractclassmethod

#A CLASSE PAI deve herdar a CLASSE ABC
class Controles(ABC):
    @abstractclassmethod
    def ligar(self):
        pass


    @abstractclassmethod
    def desligar(self):
        pass

#Sempre que utilizarmos CLASSES abstratas as CLASSES filhas devem passar o METODO da CLASSE PAI 
class Controle_TV(Controles):
    def ligar(self):
        print("Ligado!")


    def desligar(self):
        print("Desligado!")


controle = Controle_TV()
controle.ligar()
controle.desligar()