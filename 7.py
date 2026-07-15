
produtos = (
    ("Notebook", 4500),
    ("Mouse", 120),
    ("Monitor", 1300),
    ("Teclado", 250),
    ("Impressora", 900),
)
 
lista_produtos = list(produtos)
 
n = len(lista_produtos)
for i in range(n):
    for j in range(n - 1 - i):
        preco_atual = lista_produtos[j][1]
        preco_proximo = lista_produtos[j + 1][1]
        if preco_atual < preco_proximo:
            lista_produtos[j], lista_produtos[j + 1] = (
                lista_produtos[j + 1],
                lista_produtos[j],
            )
 
for posicao, produto in enumerate(lista_produtos, start=1):
    nome, preco = produto
    print(f"{posicao}º - {nome} - R$ {preco}")