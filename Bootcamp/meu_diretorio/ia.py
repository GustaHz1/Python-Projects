from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

dados = load_iris()
modelo = DecisionTreeClassifier()
modelo.fit(dados.data, dados.target)

print("Previsão:", modelo.predict([dados.data[0]]))
