class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"{self.nombre} ({self.edad} años)"

def insercion_personas(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and actual.edad < lista[j].edad:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual

personas = [Persona("Juan", 25), Persona("Ana", 30), Persona("Pedro", 20), Persona("María", 35)]
print("Lista original:")
for persona in personas:
    print(persona)

insercion_personas(personas)
print("\nLista ordenada por edad:")
for persona in personas:
    print(persona)
