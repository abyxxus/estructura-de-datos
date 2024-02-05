"""
Generar sin POO, un programa en Java que implemente un algoritmo para buscar un elemento en una matriz ordenada en filas y columnas.
La matriz estará ordenada de manera ascendente tanto en filas como en columnas. Deberás implementar un método eficiente para realizar
la búsqueda y mostrar por pantalla la posición (fila y columna) del elemento si se encuentra,
o un mensaje indicando que el elemento no está presente en la matriz.
"""

mat = [ ['1.0', '2.0', '3.0', '4.0'],
        ['1.1', '2.1', '3.1', '4.1'],
        ['1.2', '2.2', '3.2', '4.2'],
        ['1.3', '2.3', '3.3', '4.3']]

po = None
data = input()
for i in range(len(mat)):
    if po != None:
        print("dato encontrado en la posicion ", po)
        break
    for a in range(len(mat[i])):
        if po != None:
            print("dato encontrado en la posicion ", po)
            break
        if mat[i][a] == data:
            po = [i,a]

