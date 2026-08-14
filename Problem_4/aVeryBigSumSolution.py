# en este desafio, tu tienes que calcular e imprimir la suma de los
# elementos de un arreglo.
# (considerando que algunos elementos puedan ser muy grandes).
# -----------------------------------------------------------------------
# Parametros:
# int ar[n]: arreglo de enteros
# Salida:
# long: la suma de los elementos del arreglo
# -----------------------------------------------------------------------
# Ejemplo:
# ar[n] = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
# Salida:
# devuelve 5000000015
# ------------------------------------------------------------------------
# Restricciones:
# 1 <= n <= 10
# 0 <= ar[i] <= (10)^10

def array_sum(ar):
    # necesitamos una variable para ir cargando la suma de elementos del arreglo
    sum = 0

    # recorremos el arreglo, con un elemento en cada iteracion
    for el in ar:
        # sumamos el primer elemento, luego el segundo, y asi hasta terminar el arreglo
        sum += el

    # devolvemos la suma de todos los elementos del arreglo
    return sum


print(array_sum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))
