def busqueda_secuencial(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i 
    return -1  

lista = [3, 5, 1, 9, 2, 7, 4]
elemento = 2
resultado = busqueda_secuencial(lista, elemento)
if resultado != -1:
    print(f"El elemento {elemento} está en la posición {resultado}.")
else:
    print(f"El elemento {elemento} no está en la lista.")
