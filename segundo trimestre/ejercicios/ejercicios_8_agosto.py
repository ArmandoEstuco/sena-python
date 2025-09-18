"""
# ejercicio 35
while True:
    n1 = int(input("ingresa: "))
    if n1 % 7 == 0:
        print(f"{n1} es multiplo de 7")
        break

# ejercicio ??
c = {
    "nombre": input("ingresa el nombre: "),
    "telefono": input("ingresa el telefono: "),
    "email": input("ingresa el email: ")
}
print(c)

# ejercicio 47
saldo = 1000
while saldo > 0:
    cantidad = int(input(f"saldo {saldo}, ingresa monto a retirar: "))
    if cantidad <= saldo:
        saldo -= cantidad
        print(f"retiro exitoso, saldo restante: {saldo}")
    else:
        print("monto mayor al saldo disponible")
print("saldo agotado")

# ejercicio 32
suma = 0

while True:
    numero = int(input("ingresa un numero"))
    if numero == 0:
        break
    suma += numero 
print(f"la suma total es: {suma}")

# ejercicio 2
a = int(input("ingresa 1 numero: "))
b = int(input("ingresa 2 numero: "))

if a > b:
    print(f"{a} es mayor que {b}")
elif b > a:
    print(f"{b} es mayor que {a}")
else:
    print("los dos numeros son iguales")

# ejercicio 54
total = 0
while True: 
    producto = input("ingresa un producto (fin para terminar): ")
    if producto == "fin":
        break
    precio = float(input(f"ingresa el precio de {producto}: "))
    total += precio
print(f"el total de la compra es: {total}")

# ejercicio 4
compra = float(input("ingresa el valor de la compra: "))

if compra > 100000:
    descuento = compra * 0.10
    total = compra - descuento
    print(f"la compra aplica a descuento de 10%, total a pagar: {total}")
else:
    print(f"la compra no aplica a descuento, total a pagar: {compra}")

# ejercicio 41
numero = int(input("ingresa numero"))
suma = 0
while numero > 0:
    digito = numero % 10
    suma += digito
    numero //= 10
print(f"la suma de esos digitos es: {suma}")

# ejercicio 37
palabras = []
while True:
    palabra = input("ingresa una palabra: ")
    if palabra in palabras:
        print(f"la palabra '{palabra}' ya se repitio")
        break
    palabras.append(palabra)

# ejercicio ?
a = int(input("ingresa el primer numero: "))
b = int(input("ingresa el segundo numero: "))
c = int(input("ingresa el tercer numero: "))
if a >= b and a >= c:
    print(f"el mayor es {a}")
elif b >= a and b >= c:
    print(f"el mayor es {b}")
else:
    print(f"el mayor es {c}")

# ejercicio ?
estudiante = {
    "nombre": input("ingresa el nombre: "),
    "edad": int(input("ingresa la edad: ")),
    "programa": input("ingresa el programa: ")
}
print(estudiante)

# ejercicio ?
numero = int(input("ingresa un numero: "))
i = 1
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1

# ejercicio 29
diccionario = {
    "apple": "manzana",
    "house": "casa",
    "car": "carro",
    "book": "libro",
    "water": "agua"
}
print(diccionario)

# ejercicio 13
n13 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = sum(n13)
print(f"la suma de los numeros es: {suma}")
"""
