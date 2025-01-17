import pandas as pd
import plotly.express as px

# Criando a tabela e visualizando as informações
tabela = pd.read_csv("cancelamentos_sample.csv" , sep=",")
print(tabela.info())

# Configurando a tabela
# Removendo colunas
tabela = tabela.drop(columns=["CustomerID" , "idade", "sexo"])
# Removendo linhas com valores vazios
tabela = tabela.dropna()
print(tabela.info())    

# Analisando porcentagens da tabela de uma coluna especifica
print(tabela["cancelou"].value_counts())
print("Porcentagem de cancelamentos: \n")
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

# Criando o gráfico e comparando duas colunas
grafico = px.histogram(tabela, x="assinatura", color="cancelou", width=600)
# Exibindo o gráfico 
grafico.show()