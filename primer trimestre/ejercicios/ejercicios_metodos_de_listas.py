# ejercicio 1
# 1
lista1 = []
lista1.append(7)
print(lista1)
# 2
nombres = ["ana", "luis"]
nombres.append("carlos")
print(nombres)

# ejercicio 2
# 1
lista2 = [1, 2, 3]
lista2.insert(0, 99)
print(lista2)
# 2
colores = ["azul", "verde"]
colores.insert(1, "rojo")
print(colores)

# ejercicio 3
# 1
lista3 = [1, 2, 3]
lista3.extend([4, 5, 6])
print(lista3)
# 2
letras = ["a", "b"]
letras.extend("ok")
print(letras)

# ejercicio 4
# 1
frutas = ["manzana", "uva", "pera"]
frutas.remove("uva")
print(frutas)
# 2
lista4 = [1, 2, 3, 2]
lista4.remove(2)
print(lista4)

# ejercicio 5
# 1
lista5 = [1, 2, 3, 4]
lista5.pop()
print(lista5)
# 2
lista6 = ["uno", "dos", "tres"]
lista6.pop(0)
print(lista6)

# ejercicio 6
# 1
lista7 = [1, 2, 3]
lista7.clear()
print(lista7)
# 2
lista8 = [1, 2, 3, 4, 5]
lista8.clear()
print(lista8)

# ejercicio 7
# 1
frutas1 = ["manzana", "pera", "uva"]
posicion = frutas1.index("pera")
print(posicion)
# 2
numeros = [4, 5, 6, 7]
indice = numeros.index(6)
print(indice)

# ejercicio 8
# 1
lista9 = [3, 1, 3, 5, 3]
veces1 = lista9.count(3)
print(veces)
# 2
lista10 = ["a", "b", "a", "c", "a"]
veces2 = lista10.count("a")
print(veces)

# ejercicio 9
# 1
lista11 = [5, 1, 4, 2, 3]
lista11.sort()
print(lista11)
# 2
lista12 = ["z", "a", "m", "b"]
lista12.sort()
print(lista12)

# ejercicio 10
# 1
lista13 = [1, 2, 3, 4]
lista13.reverse()
print(lista13)
# 2
lista14 = ["inicio", "medio", "fin"]
lista14.reverse()
print(lista14)

# ejercicio 11
# 1
lista_original1 = [1, 2, 3]
copia_lista1 = lista_original1.copy()
print(copia_lista1) 
# 2
lista_original2 = ["a", "b", "c"]
copia_lista1 = lista_original2.copy()
copia_lista1.append("d")
print(lista_original2)
print(copia_lista1)