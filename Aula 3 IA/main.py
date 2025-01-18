import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Criando a tabela e exibindo
tabela = pd.read_csv("clientes.csv", sep=",")
print("Primeiros dados da tabela:")
print(tabela.head())
print("\nInformações da tabela antes do Label Encoding:")
print(tabela.info())

# Transformando todas as colunas categóricas em valores numéricos, exceto "score_credito"
codificador = LabelEncoder()
for coluna in tabela.columns:
    if tabela[coluna].dtype == "object" and coluna != "score_credito":
        tabela[coluna] = codificador.fit_transform(tabela[coluna])

print("\nInformações da tabela após o Label Encoding:")
print(tabela.info())

# Separando a base de dados
y = tabela["score_credito"]
x = tabela.drop(["score_credito", "id_cliente"], axis=1)

# Criando variáveis de treino e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=42)

# Criando o modelo Random Forest
modelo_arvore = RandomForestClassifier()
modelo_arvore.fit(x_treino, y_treino)

# Verificando a frequência dos valores de "score_credito"
contagem_scores = tabela["score_credito"].value_counts()
print("\nFrequências de 'score_credito':")
print(contagem_scores / sum(contagem_scores))

# Verificando a precisão da IA
previsao_arvore = modelo_arvore.predict(x_teste)
print("\nAcurácia do modelo:")
print(accuracy_score(y_teste, previsao_arvore))

# Importância das variáveis no modelo
colunas = list(x_teste.columns)
importancia = pd.DataFrame(index=colunas, data=modelo_arvore.feature_importances_, columns=["Importância"])
importancia = importancia * 100
print("\nImportância das variáveis:")
print(importancia)

# Comparando valores reais e previstos
comparacao = pd.DataFrame({
    "Real": y_teste.values,
    "Previsao": previsao_arvore
})
print("\nComparação entre valores reais e previstos:")
print(comparacao)

# Salvando o DataFrame de comparação em CSV
comparacao.to_csv("comparacao_previsoes.csv", index=False)
print("\nArquivo 'comparacao_previsoes.csv' salvo com sucesso.")
