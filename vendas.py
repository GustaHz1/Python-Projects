vendas = []
total_vendas = 0
media = 0
abaixo_media = 0
i = 1

while i <= 30:
    vendas.append(i)
    i += 1
    
print(vendas)
    
    
for venda in vendas:
    total_vendas += venda
    media = total_vendas / 30

for venda in vendas:
    if venda < media:
        abaixo_media += 1

print(f"Total de vendas R${total_vendas}")
print(f"Media de vendas R${media}")
print(f"Dias abaixo da media {abaixo_media}")