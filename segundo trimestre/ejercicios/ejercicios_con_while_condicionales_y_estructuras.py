# ejercicios con while, condicionales y estructuras

# ejercicio 1: suma hasta cero
# este programa pide numeros enteros y los suma hasta que el usuario escriba 0
total1 = 0
n1 = int(input("ingresa numero entero (0 para terminar): "))
while n1 != 0:
    total1 += n1
    n1 = int(input("ingresa numero entero (0 para terminar): "))
print(f"la suma total es {total1}")

# ejercicio 2: contraseña secreta
# pide al usuario que ingrese la contraseña hasta que sea correcta
clave2 = ""
while clave2 != "armandoestuco":
    clave2 = input("ingresa la contraseña: ")
print("acceso concedido")

# ejercicio 3: lista de compras
# guarda productos en una lista hasta que el usuario escriba 'fin'
compras3 = []
producto3 = input("ingresa un producto (escribe fin para terminar): ")
while producto3 != "fin":
    compras3.append(producto3)
    producto3 = input("ingresa un producto (escribe fin para terminar): ")
print(f"tu lista de compras es: {compras3}")

# ejercicio 4: contador de pares e impares
# pide 10 numeros y cuenta cuantos son pares y cuantos son impares
pares4 = 0
impares4 = 0
contador4 = 0
while contador4 < 10:
    num4 = int(input("ingresa numero: "))
    if num4 % 2 == 0:
        pares4 += 1
    else:
        impares4 += 1
    contador4 += 1
print(f"pares: {pares4}, impares: {impares4}")

# ejercicio 5: promedio de calificaciones
# pide notas hasta que el usuario escriba 'salir' y calcula el promedio
notas5 = []
entrada5 = input("ingresa una nota entre 0 y 5 (o escribe salir): ")
while entrada5 != "salir":
    nota5 = float(entrada5)
    if 0 <= nota5 <= 5:
        notas5.append(nota5)
    entrada5 = input("ingresa una nota entre 0 y 5 (o escribe salir): ")
if len(notas5) > 0:
    promedio5 = sum(notas5) / len(notas5)
    print(f"el promedio de notas es {promedio5}")
else:
    print("no se ingresaron notas")

# ejercicio 6: tabla de multiplicar interactiva
# pide un numero y muestra su tabla de multiplicar del 1 al 10
num6 = int(input("ingresa numero para ver su tabla: "))
i6 = 1
while i6 <= 10:
    print(f"{num6} x {i6} = {num6 * i6}")
    i6 += 1

# ejercicio 7: adivina el numero
# el usuario tiene que adivinar un numero secreto
secreto7 = 17
intento7 = int(input("adivina el numero: "))
while intento7 != secreto7:
    if intento7 < secreto7:
        print("el numero es mayor")
    else:
        print("el numero es menor")
    intento7 = int(input("intenta de nuevo: "))
print("felicidades, adivinaste el numero")

# ejercicio 8: tupla de frutas
# el usuario debe adivinar una fruta dentro de la tupla
frutas8 = ("manzana", "pera", "uva", "naranja")
fruta8 = ""
while fruta8 not in frutas8:
    fruta8 = input("adivina una fruta: ")
print(f"correcto, {fruta8} esta en la tupla")

# ejercicio 9: diccionario de traduccion
# el usuario ingresa una palabra en espanol y muestra su traduccion si existe
traducciones9 = {
    "hola": "hello",
    "perro": "dog",
    "gato": "cat",
    "casa": "house",
    "libro": "book"
}
palabra9 = input("ingresa una palabra en espanol (o salir): ")
while palabra9 != "salir":
    if palabra9 in traducciones9:
        print(f"la traduccion de {palabra9} es {traducciones9[palabra9]}")
    else:
        print("palabra no encontrada")
    palabra9 = input("ingresa una palabra en espanol (o salir): ")

# ejercicio 10: calculadora basica
# permite al usuario elegir una operacion matematica
opcion10 = 0
while opcion10 != 5:
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. salir")
    opcion10 = int(input("elige una opcion: "))
    if opcion10 >= 1 and opcion10 <= 4:
        a10 = float(input("ingresa el primer numero: "))
        b10 = float(input("ingresa el segundo numero: "))
        if opcion10 == 1:
            print(f"resultado: {a10 + b10}")
        elif opcion10 == 2:
            print(f"resultado: {a10 - b10}")
        elif opcion10 == 3:
            print(f"resultado: {a10 * b10}")
        elif opcion10 == 4:
            if b10 != 0:
                print(f"resultado: {a10 / b10}")
            else:
                print("no se puede dividir entre cero")

# ejercicio 11: registro de edades
# guarda nombres y edades en un diccionario hasta que el usuario escriba salir
personas11 = {}
nombre11 = input("ingresa un nombre (o salir): ")
while nombre11 != "salir":
    edad11 = int(input(f"ingresa la edad de {nombre11}: "))
    personas11[nombre11] = edad11
    nombre11 = input("ingresa un nombre (o salir): ")
print(f"registro de personas: {personas11}")

# ejercicio 12: buscar en lista
# el usuario escribe colores hasta que acierte uno de la lista
colores12 = ["rojo", "azul", "verde", "amarillo", "negro"]
color12 = ""
while color12 not in colores12:
    color12 = input("escribe un color: ")
print(f"correcto, {color12} esta en la lista")

# ejercicio 13: potencias de un numero
# pide un numero y muestra sus potencias del 1 al 5
num13 = int(input("ingresa un numero: "))
exp13 = 1
while exp13 <= 5:
    print(f"{num13} elevado a {exp13} = {num13 ** exp13}")
    exp13 += 1

# ejercicio 14: lista de cuadrados
# pide 5 numeros y guarda sus cuadrados en una lista
cuadrados14 = []
contador14 = 0
while contador14 < 5:
    n = int(input("ingresa un numero: "))
    cuadrados14.append(n ** 2)
    contador14 += 1
print(f"la lista de cuadrados es {cuadrados14}")

# ejercicio 15: diccionario de estudiantes
# registra estudiantes con su nota final hasta que se escriba fin
estudiantes15 = {}
nombre15 = input("ingresa nombre del estudiante (o fin): ")
while nombre15 != "fin":
    nota15 = float(input(f"ingresa la nota de {nombre15}: "))
    estudiantes15[nombre15] = nota15
    nombre15 = input("ingresa nombre del estudiante (o fin): ")
print(f"registro de estudiantes: {estudiantes15}")
