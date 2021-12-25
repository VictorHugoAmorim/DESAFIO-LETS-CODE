from random import randint
lista = []

for num in range(10):
    lista.append(randint(1,9))
    if lista[num] % 2 == 0:
        print(f'{lista[num]} é par')
    else:
        print(f'{lista[num]} é impar')
print(lista)

