# LAB 02 EJERCICIO 02
# PUNTO 1

numeros = [2, 5, 10, 11, 15, 20]
palabras = ["sol", "computador", "python", "agua", "reloj", "ala"]
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# a. 
comp_a = [(n, n**2) for n in numeros]
# b. 
comp_b = [n**3 for n in numeros if n > 10]
# c. 
comp_c = [n for n in numeros if n % 2 == 0]
# d. 
comp_d = [f"valor: {n}" for n in numeros]
# e.
comp_e = [c * 1.8 + 32 for c in numeros]
# f. 
comp_f = [p for p in palabras if len(p) > 5]
# g. 
comp_g = [p[0] for p in palabras]
# h. 
comp_h = ["par" if n % 2 == 0 else "impar" for n in numeros]
# i. 
comp_i = [elemento for fila in matriz for elemento in fila]
print("a.", comp_a)
print("b.", comp_b)
print("c.", comp_c)
print("d.", comp_d)
print("e.", comp_e)
print("f.", comp_f)
print("g.", comp_g)
print("h.", comp_h)
print("i.", comp_i)