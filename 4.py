# 4. Contagem e posição em tupla

numeros = (1, 2, 3, 2, 4, 2, 5)
 
qtd_dois = numeros.count(2)
posicao_quatro = numeros.index(4)
 
print(f"Tupla: {numeros}")
print(f"O número 2 aparece {qtd_dois} vezes")
print(f"A primeira ocorrência de 4 está na posição {posicao_quatro}")
print()