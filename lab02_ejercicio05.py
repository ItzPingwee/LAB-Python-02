#LAB 02 EJERCICIO 05
# PUNTO 1
lista_combinada = [2, 5, 8, 11, 20, 50]

# a. Filtrar números pares y luego elevarlos al cuadrado
comb_a = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, lista_combinada)))
print("a.", comb_a)
# b. Elevar al cubo, filtrar mayores a 100, convertir a cadenas
comb_b = list(map(str, filter(lambda x: x > 100, map(lambda x: x**3, lista_combinada))))
print("b.", comb_b)
# c. Filtrar mayores a 10, elevar al cuadrado, ordenar de mayor a menor
filtrados_y_cuadrados = list(map(lambda x: x**2, filter(lambda x: x > 10, lista_combinada)))
comb_c = sorted(filtrados_y_cuadrados, reverse=True)
print("c.", comb_c)