"""
Haciendo uso de estructuras de datos estáticos (vectores y matrices) sin POO,
Escribe un programa en Java que transponga, en sentido antihorario,
una matriz cuadrada de 4x4. Se deberá hacer la rotación en su lugar, es decir, sin utilizar matrices auxiliares.
"""

mat = [ ['1.0', '2.0', '3.0', '4.0'],
        ['1.1', '2.1', '3.1', '4.1'],
        ['1.2', '2.2', '3.2', '4.2'],
        ['1.3', '2.3', '3.3', '4.3']]

"""for i in range(len(mat)):
    for a in range(4):
        mat[i].append(input("ingrese un datos:\t"))"""

def vol(mat):
    for i in range(-1,-(len(mat)+1),-1):
        a = mat.pop(i)
        mat.append(a)
    return (mat)

mat = vol(mat)
for i in range(len(mat)):
    mat[i] = vol(mat[i])

for i in mat:
    print(i)