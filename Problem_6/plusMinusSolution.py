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
    n = len(arr)  # el numero de elementos que hay en el arreglo
    count_positives = 0  # una variable para contar cuantos elementos positivos hay
    count_negatives = 0  # una variable para contar cuantos elementos negativos hay
    count_zero = 0  # una variable para contar cuantos ceros hay

    # por cada elemento dentro del arreglo
    for item in arr:
        # si el elemento es mayor a cero
        if item > 0:
            count_positives += 1  # incremento 1 a los positivos
        # si el elemento es menor a cero
        elif item < 0:
            count_negatives += 1  # incremento 1 a los negativos
        # si no es positivo ni negativo
        else:
            count_zero += 1  # incremento 1 a los valores iguales a cero

    # redondeo con la funcion round() y marco 6 lugares despues de la coma
    positives_ratio = round(count_positives / n, 6)
    negatives_ratio = round(count_negatives / n, 6)
    zero_ratio = round(count_zero / n, 6)

    # imprimo los radios cada uno en una linea aparte
    print(positives_ratio)
    print(negatives_ratio)
    print(zero_ratio)


print(plus_minus([1, 1, 0, -1, -1]))
print("\n")
print(plus_minus([-4, 3, -9, 0, 4, 1]))
