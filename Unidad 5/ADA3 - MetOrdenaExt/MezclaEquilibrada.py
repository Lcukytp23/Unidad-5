def mezcla_equilibrada(lista):
    if len(lista) <= 1:
        return lista

    listas = distribuir(lista)
    print(f'Fase de distribución: {listas}')

    paso = 1
    while len(listas) > 1:
        nuevas_listas = []
        for i in range(0, len(listas), 2):
            if i + 1 < len(listas):
                nueva_lista = intercalacion(listas[i], listas[i+1])
                nuevas_listas.append(nueva_lista)
                print(f'Paso {paso}, intercalando: {listas[i]} y {listas[i+1]} en {nueva_lista}')
            else:
                nuevas_listas.append(listas[i])
                print(f'Paso {paso}, sublista sin cambio: {listas[i]}')
        listas = nuevas_listas
        paso += 1

    return listas[0]

def distribuir(lista):
    sublistas = []
    for i in range(0, len(lista), 2):
        if i + 1 < len(lista):
            sublistas.append([lista[i], lista[i+1]])
        else:
            sublistas.append([lista[i]])
    for sublista in sublistas:
        sublista.sort()
    return sublistas

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
ordenada = mezcla_equilibrada(lista)
print(f'Lista ordenada: {ordenada}')
