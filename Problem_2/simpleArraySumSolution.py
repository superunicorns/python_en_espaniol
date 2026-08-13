# Dado un arreglo de enteros. encuentra la suma de sus elementos.
# Ejemplo:
# ar = [1, 2, 3]
# 1 + 2 + 3 = 6
# Output:
# devuelve 6
# ----------------------------------------------------------------------------
# ar[n]: arreglo de enteros
# int: la suma de los elementos del arreglo
# ----------------------------------------------------------------------------
# Restricciones:
# 0 < n, ar[i] <= 1000

def simple_array_sum(ar):
    # primero necesitamos una variable para acumular la suma de los elementos.
    sum = 0

    # luego iteramos el arreglo y sumamos un elemento en cada iteracion
    for item in ar:
        sum += item

    # luego devolvemos la suma de todos los elementos
    return sum


print(simple_array_sum([1, 2, 3]))  # 6
print(simple_array_sum([1, 2, 3, 4, 10, 11]))  # 31
