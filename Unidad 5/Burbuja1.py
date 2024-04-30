import random

def insercion(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and actual < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual

numeros_aleatorios = [random.randint(1, 100) for _ in range(10)]
print("Lista original:", numeros_aleatorios)

insercion(numeros_aleatorios)
print("Lista ordenada:", numeros_aleatorios)
