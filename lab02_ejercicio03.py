# LAB 02 EJERCICIO 3
# PUNTO 1
celsius = [0, 20, 30, 42]
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
radios = [1, 2, 5]
precios = {"pan": 1000, "leche": 2500, "café": 5000}
matriz_num = [[1, 2], [3, 4]]
# a. 
map_a = list(map(lambda c: c * 1.8 + 32, celsius))
print("a.", map_a)
# b.
map_b = list(map(lambda x, y: x + y, lista1, lista2))
print("b.", map_b)
# c. 
map_c = list(map(lambda r: 3.1415 * (r**2), radios))
print("c.", map_c)
# d. 
map_d = list(map(lambda item: (item[0], item[1] * 1.10), precios.items()))
print("d.", map_d)
# e. 
map_e = list(map(lambda fila: list(map(lambda x: x * 10, fila)), matriz_num))
print("e.", map_e)