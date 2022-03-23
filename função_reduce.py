

from functools import reduce

lista = [2,8,9,10,67]

def mult(x,y):
    return x*y
print(reduce(mult,lista))



lista2 =[45,1,78,23,89]

testamaior = lambda x,y: x if (x>y) else y

print(reduce(testamaior,lista2))

