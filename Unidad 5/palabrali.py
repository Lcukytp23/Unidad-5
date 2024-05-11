def insercion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and len(key) < len(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

palabras = ["manzana", "banana", "pera", "uva", "kiwi"]
print("Lista por ordenar:")
print(palabras)
insercion(palabras)
print("Palabras ordenadas por longitud:")
print(palabras)
