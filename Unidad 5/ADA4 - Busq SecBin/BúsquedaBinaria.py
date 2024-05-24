def busqueda_binaria(lista, elemento):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio 
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  

lista_ord = [1, 2, 3, 4, 5, 7, 9]
elemento = 7
resultado = busqueda_binaria(lista_ord, elemento)
if resultado != -1:
    print(f"El elemento {elemento} está en la posición {resultado}.")
else:
    print(f"El elemento {elemento} no está en la lista.")
