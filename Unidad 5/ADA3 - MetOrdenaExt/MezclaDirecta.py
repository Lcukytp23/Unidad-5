def mezcla_directa(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    print(f'Dividiendo: {lista[:medio]} y {lista[medio:]}')
    izquierda = mezcla_directa(lista[:medio])
    derecha = mezcla_directa(lista[medio:])

    resultado = intercalacion(izquierda, derecha)
    print(f'Intercalando: {izquierda} y {derecha} en {resultado}')
    return resultado

def intercalacion(lista1, lista2):
    i, j = 0, 0
    resultado = []
    
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    while i < len(lista1):
        resultado.append(lista1[i])
        i += 1
        
    while j < len(lista2):
        resultado.append(lista2[j])
        j += 1
        
    return resultado

lista = [38, 27, 43, 3, 9, 82, 10]
print(f'Lista original: {lista}')
ordenada = mezcla_directa(lista)
print(f'Lista ordenada: {ordenada}')
