class TablaHash:
    def __init__(self, size):
        self.size = size
        self.tabla = [None] * size

    def agregar(self, clave, valor):
        indice = hash(clave) % self.size
        if self.tabla[indice] is None:
            self.tabla[indice] = [(clave, valor)]
        else:
            for i, (k, v) in enumerate(self.tabla[indice]):
                if k == clave:
                    self.tabla[indice][i] = (clave, valor)
                    break
            else:
                self.tabla[indice].append((clave, valor))

    def buscar(self, clave):
        indice = hash(clave) % self.size
        if self.tabla[indice] is not None:
            for k, v in self.tabla[indice]:
                if k == clave:
                    return v
        return None

tabla = TablaHash(10)
tabla.agregar('a', 1)
tabla.agregar('b', 2)
tabla.agregar('c', 3)

print(tabla.buscar('b'))  
print(tabla.buscar('d'))  
