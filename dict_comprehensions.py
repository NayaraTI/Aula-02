## Tem a mesma lógica da list comprehension só que em dicionário ##

listadic = [
    ('valor1',10),
    ('valor2',8),
    ('valor3',30),
]

listadic.sort ## colocar em ordem alfabética

d1 = {c:v for c,v in listadic}

print(d1)

d2 = {c:v*2 for c,v in listadic}

print(d2)

d3 = {c.upper():v for c,v in listadic} ## letra maiúscula

print(d3)      