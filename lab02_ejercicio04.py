from functools import reduce
# LAB 02 EJERCICIO 04
# EJERCICIO 01 FILTER
palabras_f = ["ala", "casa", "python", "elefante", "ojo", "oso"]
valores = [1, None, "hola", None, 5]
numeros_f = [5, 15, 23, 35, 40, 55]
productos = [
    {"nombre": "Teclado", "precio": 80},
    {"nombre": "Mouse", "precio": 40},
    {"nombre": "Monitor", "precio": 300},
    {"nombre": "Webcam", "precio": 150}
]

# a. 
filter_a = list(filter(lambda p: len(p) > 4, palabras_f))
print("a.", filter_a)
# b. 
filter_b = list(filter(lambda x: x is not None, valores))
print("b.", filter_b)
# c. 
filter_c = list(filter(lambda p: p.lower()[0] in 'aeiouáéíóú', palabras_f))
print("c.", filter_c)
# d. 
filter_d = list(filter(lambda p: p.lower() == p.lower()[::-1], palabras_f))
print("d.", filter_d)
# e. 
filter_e = list(filter(lambda n: n % 10 == 5, numeros_f))
print("e.", filter_e)
# f. 
filter_f = list(filter(lambda prod: prod["precio"] > 100, productos))
print("f.", filter_f)
# -------------------------------------------------------------------------
# EJERCICIOS DE REDUCE
numeros_r = [1, 2, 3, 4, 5]
palabras_r = ["Hola", " ", "Mundo", "!"]

# a. 
reduce_a = reduce(lambda x, y: x * y, numeros_r)
print("a.", reduce_a)
# b.
reduce_b = reduce(lambda x, y: x + y, palabras_r)
print("b.", reduce_b)
# c. 
def mayor_de_dos(a, b):
    return a if a > b else b
reduce_c = reduce(mayor_de_dos, numeros_r)
print("c.", reduce_c)
#---------------------------------------------------------------------------
# EJERCICIOS DE SORTED
palabras_s = ["pera", "manzana", "uva", "kiwi"]
tuplas_s = [(3, "tres"), (1, "uno"), (2, "dos")]
productos_s = [
    ("Camisa", 30),
    ("Pantalón", 55),
    ("Medias", 10),
    ("Chaqueta", 80)
]
empleados = [
    ("Maria", "Ventas", 30),
    ("Luis", "Tecnología", 25),
    ("Ana", "Ventas", 25),
    ("Pedro", "Tecnología", 28)
]
# a.
sorted_a = sorted(palabras_s)
print("a.", sorted_a)
# b.
sorted_b = sorted(tuplas_s, key=lambda x: x[0])
print("b.", sorted_b)
# c.
sorted_c = sorted(productos_s, key=lambda x: (-x[1], x[0]))
print("c.", sorted_c)
# d.
sorted_d = sorted(palabras_s, key=len)
print("d.", sorted_d)
# e. 
nums_s = [7, 2, 9, 4, 1, 6]
sorted_e = sorted(nums_s, key=lambda x: x % 2)
print("e.", sorted_e)
# f. 
palabra_f = "esternocleidomastoideo"
frecuencias = {letra: palabra_f.count(letra) for letra in set(palabra_f)}
sorted_f = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
print("f.", sorted_f)
# g. 
sorted_g = sorted(empleados, key=lambda x: (x[1], x[2]))
print("g.", sorted_g)