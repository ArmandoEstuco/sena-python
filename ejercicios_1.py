
# ejercicio 1: registrar 3 frutas

frutas = []

for i in range(3):
    fruta = input("escribe el nombre de una fruta: ")
    frutas.append(fruta)

print("lista de frutas:", frutas)



# ejercicio 2: guardar 2 edades

edades = []

for i in range(2):
    edad = int(input("ingresa una edad: "))
    edades.append(edad)

print("edades almacenadas:", edades)



# ejercicio 3: notas de dos estudiantes

notas = []

for i in range(2):
    nota = float(input("ingresa una nota: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)

print("notas ingresadas:", notas)
print("promedio de notas:", promedio)



# ejercicio 4: productos en una bolsa

productos = []

for i in range(3):
    producto = input("isngresa el nombre de un producto: ")
    productos.append(producto)

print("productos en la bolsa:", productos)



# ejercicio 5: precios de 3 articulos

precios = []

for i in range(3):
    precio = float(input("ingresa el precio de un articulo: "))
    precios.append(precio)

suma_total = sum(precios)

print("precios:", precios)
print("suma total:", suma_total)



# ejercicio 6: numeros ingresados por el usuario

numeros = []

for i in range(4):
    numero = float(input("ingresa un numero: "))
    numeros.append(numero)

mayor = max(numeros)
menor = min(numeros)

print("numeros ingresados:", numeros)
print("numero mayor:", mayor)
print("numero menor:", menor)
