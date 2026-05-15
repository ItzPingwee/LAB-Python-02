# LAB 02 PUNTO 1
# EJERCICIO 01
es_multiplo3 = lambda x: x % 3 == 0
print(es_multiplo3(9))
num_al_cubo = lambda x: x**3
print(num_al_cubo(3))
producto_xy = lambda x, y: x*y
print(producto_xy(2, 3))
mayor_num = lambda x, y: x if x>y else y
print(mayor_num(5, 7))
empieza_con_a = lambda x: x.lower().startswith("a")
print(empieza_con_a("Arbol"))
celsius_a_fahrenheit = lambda c: c * 1.8 + 32
print(celsius_a_fahrenheit(18))
# EJERCICIO 02
operaciones = [
    lambda x: x * 2, 
    lambda x: x + 10,
    lambda x: x ** 2 
]
num = int(input("Ingrese un número: "))
for operacion in operaciones:
    print(operacion(num))