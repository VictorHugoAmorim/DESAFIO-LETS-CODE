from random import randint
lista1 = []
lista2 = []
resultado = []

for num in range(10):
    lista1.append(randint(0,9))
    lista2.append(randint(0,9))
    resultado.append(lista1[num] + lista2[num])

print(f'{lista1}\n{lista2}\n{resultado}')

