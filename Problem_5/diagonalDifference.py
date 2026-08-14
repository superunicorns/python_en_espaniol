# Dada una matriz cuadrada, calcula la diferencia en valor absoluto de
# la suma de los elementos de sus diagonales.
# ----------------------------------------------------------------------
# Ejemplo:
# tenemos la siguiente matriz abajo de esta linea
# 1    2    3
# 4    5    6
# 9    8    9
# la diagonal de izquierda a derecha (diagonal principal) =
# 1 + 5 + 9 = 15
# la diagonal de derecha a izquierda (anti diagonal) =
# 3 + 5 + 9 = 17
# la diferencia absoluta es |15 - 17| = 2
# -----------------------------------------------------------------------
# Parametros:
# int arr[n][m]: arreglo 2D de enteros
# Salida:
# int: la diferencia absoluta de la suma de las diagonales.
# -----------------------------------------------------------------------
# Restricciones:
# -100 <= arr[i][j] <= 100

def diagonal_difference(arr):
  # escribe tu codigo aqui en esta linea


print(diagonal_difference([[1, 2, 3], [4, 5, 6], [9, 8, 9]]))  # salida: 2
print(diagonal_difference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))  # salida: 15
