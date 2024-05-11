def burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

nombres = ["Juan", "Ana", "Pedro", "María", "Carlos"]
print("Nombres antes de ordenar")
print(nombres)
burbuja(nombres)
print("Nombres ordenados alfabéticamente:")
print(nombres)
