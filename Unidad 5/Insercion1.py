def insercion(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and actual < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual

numeros = [64, 34, 25, 12, 22, 11, 90]
insercion(numeros)
print("Lista ordenada:", numeros)
