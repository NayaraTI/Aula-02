## Função MAP aplica uma ação em uma estrutura de dados
# E retorna os elementos com a ação aplicada

## 1 Elemento

lista =[1,4,6,5,8]

def soma(x):
    return x+2

print(list(map(soma,lista)))