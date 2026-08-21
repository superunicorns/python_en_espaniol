# Starcaise detalles
# Esta es una escalera de tamaño n = 4.
# Escribe un programa que imprima una escalera de tamaño n = 4.
# Todas las lineas deben estar alineadas a la derecha.
# ----------------------------------------------------------------------
# Ejemplo:
# n = 4
# Salida:
#       #
#     # #
#   # # #
# # # # #
# La base y la altura son ambos igual a n.
# Esta dibujado usando # simbolos y espacios.
# La ultima linea no debe estar precedida por ningun espacio.
# ----------------------------------------------------------------------
# Parametros:
# int n: un entero.
# imprime una escalera, la funcion no deberia retornar ningun valor.
# ----------------------------------------------------------------------
# Restricciones:
# 0 < n <= 100

def staircaise(n):
    # tenemos un indice i de 1 hasta n + 1
    for i in range(1, n + 1):
        # imprimimos la cantidad de espacio mas la cantidad de #
        # alineados a la derecha
        print(" " * (n - i) + "#" * i)


print(staircaise(4))
