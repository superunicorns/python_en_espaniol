# Para Alicia y Bob se creo un desafio de HackerRank para cada uno.
# Un profesor califico ambos desafios, otorgando puntos en una
# escala del 1 al 100 para tres categorías: claridad del problema,
# originalidad y dificultad.
# La calificacion para el desafio de Alicia es el
# triple a = (a[0], a[1], a[2]) y la calificacion para el desafio
# de Bob es el triple b = (b[0], b[1], b[2])
# La tarea es comparar quien gano comparando cada categoria.
# if a[i] > b[i] entonces Alicia gana 1 punto.
# if a[i] < b[i] entonces Bob gana 1 punto.
# if a[i] == b[i] entonces es un empate y ninguno gana puntos.
# --------------------------------------------------------------------
# Ejemplo:
# a = (5, 6, 7)
# b = (3, 6, 10)
# Output:
# devuelve [1, 1]
# ---------------------------------------------------------------------
# Restricciones:
# 1 <= a[i] <= 100
# 1 <= b[i] <= 100

def compare_triplets(a, b):
    # primero necesitamos variables para los puntos
    alicia_puntos = 0
    bob_puntos = 0

    # recorrer el arreglo con un for loop
    for i in range(len(a)):
        # si a[i] es mayor que b[i]
        if a[i] > b[i]:
            alicia_puntos += 1  # suma 1 punto a Alicia
        # si a[i] menor que b[i]
        elif a[i] < b[i]:
            bob_puntos += 1  # suma 1 punto a Bob
        # si no
        else:
            # No sumar puntos
            alicia_puntos += 0
            bob_puntos += 0

    return [alicia_puntos, bob_puntos]


print(compare_triplets([5, 6, 7], [3, 6, 10]))  # [1, 1]
print(compare_triplets([17, 28, 30], [99, 16, 8]))  # [2, 1]
