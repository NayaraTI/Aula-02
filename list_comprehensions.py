## Manipulação de listas de forma simplificada
## PEP 202

listanumeros = [1,4,5,6,160]

lc1 = [multiplica*2 for multiplica in listanumeros]

print(lc1)


listapares = [p for p in range(20) if p % 2 == 0]

print(listapares)

listanome = ["João","Alberto","Juca","Afonso"]

lc2 = [troca.replace('a','@') for troca in listanome]

print(lc2)