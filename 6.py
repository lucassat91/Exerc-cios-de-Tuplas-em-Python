# 6. Números repetidos e suas contagens

numeros = (5, 2, 8, 2, 9, 2, 5, 7, 8, 5)
 
ja_processados = []
 
for numero in numeros:
    if numero not in ja_processados:
        qtd = numeros.count(numero)
        if qtd > 1:
            print(f"{numero} aparece {qtd} vezes")
        ja_processados.append(numero)
print()
 