import pandas as pd

# Lendo o Dataframe
tabela = pd.read_excel('challenge.xlsx')
print(tabela.columns)

# Enviando as informações
#driver.find_element(By.XPATH, "//input[@ng-reflect-name = 'labelCompanyName']")