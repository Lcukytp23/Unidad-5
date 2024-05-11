def seleccion(arr, key=None):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if key:
                if key(arr[j]) < key(arr[min_idx]):
                    min_idx = j
            else:
                if arr[j] < arr[min_idx]:
                    min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

estudiantes = [("Daniel", 85), ("Javi", 70), ("Manuel", 95), ("Ader", 0)]
print("Calificaciones antes de ser ordenadas:")
print(estudiantes)
seleccion(estudiantes, key=lambda x: x[1])
print("Estudiantes ordenados por calificaciones:")
print(estudiantes)
