from langchain.llms import OpenAI
llm = OpenAI(api_key='sua-chave-aqui')
resposta = llm("Me diga 3 curiosidades sobre IA")
print(resposta)
