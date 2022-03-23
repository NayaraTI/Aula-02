
dicverduras = {1:"Cebola",2:"Alface",3:"Repolho",4:"Beterraba"}
dicfrutas = {1:"Maçã",2:"Laranja",3:"Pera"}

juntavalores = list(zip(dicverduras.values(),dicfrutas.values()))

print(juntavalores)


## iterar o elemento

for p in juntavalores:
    print(p)