def burbuja(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", numeros)

burbuja(numeros)
print("Lista ordenada:", numeros)
