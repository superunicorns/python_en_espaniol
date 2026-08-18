# Dado un arreglo de enteros, calcula los radios de sus elementos
# los que son positivos, negativos y cero. Imprime el valor decimal
# de cada fraccion en una nueva linea con 6 lugares despues de la coma.
# ---------------------------------------------------------------------------
# Ejemplo:
# arr = [1, 1, 0, -1, -1]
# el arreglo tiene n = 5 elementos, dos positivos, dos negativos y un cero.
# Los radios son 2/5 = 0.400000, 2/5 = 0.400000 y 1/5 = 0.200000.
# Salida:
# 0.4
# 0.4
# 0.2
# ----------------------------------------------------------------------------
# Parametros:
# int arr[n]: arreglo de enteros.
# ----------------------------------------------------------------------------
# Restricciones:
# 0 < n <= 100
# -100 <= arr[i] <= 100

def plus_minus(arr):
  # escribe tu codigo aqui en esta linea


print(plus_minus([1, 1, 0, -1, -1]))
print("\n")
print(plus_minus([-4, 3, -9, 0, 4, 1]))
