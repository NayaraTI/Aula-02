
## Função filter filtrar e separa um elemento solicitado
# Trazendo na saída

lista_mista = [1,"João",56,"Pedro",67]

def valida(x):
    return x == "João"

print(list(filter(valida,lista_mista)))

print(list(filter(lambda x: x == "Pedro",lista_mista)))