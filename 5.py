# 5. Análise de vendas

vendas = (1500, 2300, 1800, 2900, 3200, 2100, 1700)
 
maior_venda = max(vendas)
menor_venda = min(vendas)
media_vendas = sum(vendas) / len(vendas)
 
acima_da_media = 0
for venda in vendas:
    if venda > media_vendas:
        acima_da_media += 1
 
print(f"Vendas: {vendas}")
print(f"a) Maior venda: {maior_venda}")
print(f"b) Menor venda: {menor_venda}")
print(f"c) Média das vendas: {media_vendas:.2f}")
print(f"d) Vendas acima da média: {acima_da_media}")
print()
 