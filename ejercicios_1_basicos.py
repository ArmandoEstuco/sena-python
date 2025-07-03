# ejercicio 1: registrar 3 frutas

frutas = []

frutas.append(input("ingresa la primera fruta: "))
frutas.append(input("ingresa la segunda fruta: "))
frutas.append(input("ingresa la tercera fruta: "))

print(f"lista de frutas: {frutas}")


# ejercicio 2: guardar 2 edades

edades = []

edades.append(int(input("ingresa la primera edad: ")))
edades.append(int(input("ingresa la segunda edad: ")))

suma_edades = edades[0] + edades[1]

print(f"edades almacenadas: {edades}")
print(f"suma de edades: {suma_edades}")


# ejercicio 3: notas de dos estudiantes

notas = []

notas.append(float(input("ingresa la primera nota: ")))
notas.append(float(input("ingresa la segunda nota: ")))

suma_notas = notas[0] + notas[1]
promedio = suma_notas / 2

print(f"notas ingresadas: {notas}")
print(f"suma de notas: {suma_notas}")
print(f"promedio de notas: {promedio}")


# ejercicio 4: productos en una bolsa

productos = []

productos.append(input("ingresa el primer producto: "))
productos.append(input("ingresa el segundo producto: "))
productos.append(input("ingresa el tercer producto: "))

print(f"productos en la bolsa: {productos}")


# ejercicio 5: precios de 3 artículos

precios = []

precios.append(float(input("ingresa el precio del primer artículo: ")))
precios.append(float(input("ingresa el precio del segundo artículo: ")))
precios.append(float(input("ingresa el precio del tercer artículo: ")))

suma_precios = precios[0] + precios[1] + precios[2]

print("precios:", precios)
print(f"suma total: {suma_precios}")


# ejercicio 6: números ingresados por el usuario
numeros = []

numeros.append(float(input("ingresa el primer número: ")))
numeros.append(float(input("ingresa el segundo número: ")))
numeros.append(float(input("ingresa el tercer número: ")))
numeros.append(float(input("ingresa el cuarto número: ")))

mayor = max(numeros)
menor = min(numeros)

print(f"numero mayor: {mayor}")
print(f"numero menor: {menor}")



# ejercicio 7: registrar 2 nombres completos

nombres = []

nombres.append("ingresa un nombre: ")
nombres.append("ingresa otro nombre: ")

print(f"hola, {nombres[0]}")
print(f"hola, {nombres[1]}")



# ejercicio 8: registrar dos temperaturas

temperaturas = []

temperaturas.append(float(input("ingresa la primera temperatura en celsius: ")))
temperaturas.append(float(input("ingresa la segunda temperatura en celsius: ")))

fahrenheit1 = (temperaturas[0] * 9/5) + 32
fahrenheit2 = (temperaturas[1] * 9/5) + 32

print(f"la primera temperatura en fahrenheit es: {fahrenheit1}")
print(f"la segunda temperatura en fahrenheit es: {fahrenheit2}")
