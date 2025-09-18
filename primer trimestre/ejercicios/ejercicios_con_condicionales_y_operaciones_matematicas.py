# Ejercicios con Condicionales y Operaciones Matemáticas

# 1. Verifica si un número es positivo, negativo o cero. 
num1 = int(input("ingresar numero: "))
if num1 > 0:
    print(f"{num1} es positivo")
elif num1 < 0:
    print(f"{num1} es negativo")
else:
    print(f"{num1} es cero")

# 2. Calcula el mayor de dos números ingresados. 
num2a = int(input("ingresar primer numero: "))
num2b = int(input("ingresar segundo numero: "))
if num2a > num2b:
    print(f"el mayor es {num2a}")
elif num2b > num2a:
    print(f"el mayor es {num2b}")
else:
    print("los dos numeros son iguales")

# 3. Determina si un número es par o impar. 
num3 = int(input("ingresar numero: "))
if num3 % 2 == 0:
    print(f"{num3} es par")
else:
    print(f"{num3} es impar")

# 4. Dado un número, verifica si está entre 10 y 20.
num4 = int(input("ingresar numero: "))
if num4 >= 10 and num4 <= 20:
    print(f"{num4} esta entre 10 y 20")
else:
    print(f"{num4} no esta entre 10 y 20")

# 5. Dados tres números, encuentra el mayor usando condicionales.
num5a = int(input("ingresar primer número: "))
num5b = int(input("ingresar segundo número: "))
num5c = int(input("ingresar tercer número: "))
if num5a >= num5b and num5a >= num5c:
    print(f"el mayor es {num5a}")
elif num5b >= num5a and num5b >= num5c:
    print(f"el mayor es {num5b}")
else:
    print(f"el mayor es {num5c}")

# 6. Calcula el precio final con un 10% de descuento si el total es mayor a $100.
total6 = float(input("ingresar total: "))
if total6 > 100:
    total6 = total6 * 0.9
print(f"el precio final es ${total6:.2f}")

# 7. Verifica si una persona puede votar (mayor o igual a 18 años). 
edad7 = int(input("ingresar edad: "))
if edad7 >= 18:
    print("puede votar")
else:
    print("no puede votar")

# 8. Dado el precio y tipo de cliente (VIP o normal), aplica un descuento del 20% solo a VIP.
precio8 = float(input("ingresar precio: "))
cliente8 = input("ingresar tipo cliente (vip o normal): ")
if cliente8.lower() == "vip":
    precio8 = precio8 * 0.8
print(f"precio final ${precio8:.2f}")

# 9. Determina si un número es múltiplo de 5 y de 3 al mismo tiempo.
num9 = int(input("ingresar numero: "))
if num9 % 5 == 0 and num9 % 3 == 0:
    print(f"{num9} es multiplo de 5 y 3")
else:
    print(f"{num9} no es multiplo de 5 y 3")

# 10. Dado un número, verifica si es divisible entre dos números dados.
num10 = int(input("ingresar numero a verificar: "))
div10a = int(input("ingresar primer divisor: "))
div10b = int(input("ingresar segundo divisor: "))
if div10a != 0 and div10b != 0 and num10 % div10a == 0 and num10 % div10b == 0:
    print(f"{num10} es divisible entre {div10a} y {div10b}")
else:
    print(f"{num10} no es divisible entre {div10a} y {div10b}")

# Ejercicios con Listas (con condicionales)

# 11. Crea una lista con 5 números. Si el tercer número es mayor que 10, muestra “Mayor a 10”, si no, muestra “Menor o igual a 10”. 
lista11 = [int(input("numero 1: ")),
           int(input("numero 2: ")),
           int(input("numero 3: ")),
           int(input("numero 4: ")),
           int(input("numero 5: "))
]
if lista11[2] > 10:
    print(f"{lista11[2]} mayor a 10")
else:
    print(f"{lista11[2]} menor o igual a 10")

# 12. Verifica si el número 7 está en la lista [3, 5, 7, 9]. Si está, muestra “Está en la lista”, si no, muestra “No está en la lista”.
lista12 = [3, 5, 7, 9]
if 7 in lista12:
    print("esta en lista")
else:
    print("no esta en lista")

# 13. Suma los dos primeros elementos de la lista [4, 6, 2, 8]. Si la suma es mayor que 10, muestra “Suma alta”, de lo contrario, muestra “Suma baja”.
lista13 = [4, 6, 2, 8]
suma13 = lista13[0] + lista13[1]
if suma13 > 10:
    print(f"la suma es {suma13} y es mayor a 10")
else:
    print(f"la suma es {suma13} y no es mayor a 10")

# 14. Dada la lista ["Ana", "Luis", "Pedro", "Marta"], muestra el último nombre. Si ese nombre es “Marta”, muestra “Nombre correcto”, si no, “Nombre diferente”.
nombres14 = ["ana", "luis", "pedro", "marta"]
ultimo_nombre14 = nombres14[-1]

if ultimo_nombre14 == "marta":
    print("nombre correcto")
else:
    print("nombre diferente")

# 15. Crea una lista con tres colores. Cambia el segundo color solo si es igual a "azul", y muestra la lista actualizada.
colores15 = ["rojo", "azul", "verde"]
print(f"lista de colores, {colores15}")
if colores15[1] == "azul":
    colores15[1] = input("ingresa otro color diferente a azul: ")
else:
    print("el segundo color no es azul, no se modifica")
print("Lista actualizada:", colores15)

# Ejercicios con Tuplas (con condicionales)

# 16. Crea una tupla con los valores (5, 8, 12, 20). Si el primer valor es menor que el último, muestra “Orden ascendente”, si no, “Orden descendente”. 
valores16 = (5, 8, 12, 20)
if valores16[0] < valores16[-1]:
    print("orden ascendente")
else:
    print("orden descendente")

# 17. Dada la tupla (25, 32, 28), verifica si el segundo valor es mayor a 30. Si lo es, muestra “Edad mayor a 30”, si no, “Edad menor o igual a 30”.
tupla17 = (25, 32, 28)
if tupla17[1] > 30:
    print("edad mayor a 30")
else:
    print("edad menor a 30")

# 18. Convierte la tupla (1, 2, 3) a lista, cambia el segundo valor a 10 solo si es igual a 2, luego vuelve a convertirla en tupla y muéstrala.
tupla18 = (1, 2, 3)
print(f"tupla original:, {tupla18}")
lista18 = list(tupla18)
if lista18[1] == 2:
    lista18[1] = 10
tupla18_actualizada = tuple(lista18)
print(f"tupla actualizada: {tupla18_actualizada}")

# 19. Dada la tupla (4, 9), accede al segundo valor. Si es mayor que 5, muestra “Coordenada alta”, si no, “Coordenada baja”.
tupla19 = (4, 9)
if tupla19[1] > 5:
    print("coordenada alta")
else:
    print("coordenada baja")

# 20. Compara si las tuplas (3, 4) y (3, 5) son iguales. Si lo son, muestra “Tuplas iguales”, si no, “Tuplas diferentes”. 
tupla20a = (3, 4)
tupla20b = (3, 5)
if tupla20a == tupla20b:
    print("tuplas iguales")
else:
    print("tuplas diferentes")

# Ejercicios con Diccionarios (con condicionales)

# 21. Crea un diccionario con {"nombre": "Juan", "edad": 17}. Si la edad es mayor o igual a 18, muestra “Adulto”, si no, muestra “Menor de edad”.
diccionario21 = {
    "nombre": "Juan",
    "edad": 17
}
if diccionario21["edad"] >= 18:
    print("adulto")
else: 
    print("menor de edad")

# 22. Crea un diccionario {"nombre": "Lucía", "edad": 20}. Si la edad es mayor a 18, cambia el valor de “edad” a 21. Luego muestra el diccionario.
diccionario22 = {
    "nombre": "Lucía",
    "edad": 20
}
if diccionario22["edad"] > 18:
    diccionario22["edad"] = 21
    print("diccionario actualizado:", diccionario22)
else:
    print("la edad no se modifica, sigue siendo:", diccionario22["edad"])

# 23. Crea un diccionario con {"nombre": "Carlos"}. Si la clave “ciudad” no existe, agrégala con el valor “Bogotá” y muestra el diccionario. 
diccionario23 = {
    "nombre": "carlos"
}
if "ciudad" not in diccionario23:
    diccionario23["ciudad"] = "bogota"
print(f"diccionario actualizado:, {diccionario23}")
    
# 24. Dado el diccionario {"producto": "pan", "precio": 1200}, verifica si la clave “precio” existe. Si existe, muestra su valor, si no, muestra “No hay precio”. 
diccionario24 = {
    "producto": "pan",
    "precio": 1200
}
if "precio" in diccionario24:
    print(f"el precio del {diccionario24["producto"]} es {diccionario24["precio"]}")
else:
    print("no hay precio")

# 25. Crea un diccionario con {"pan": 1200, "leche": 2000}. Si “pan” está en el diccionario, muestra su precio; si no, muestra “Producto no disponible”
diccionario25 = {
    "pan": 1200,
    "leche": 2000
}
if "pan" in diccionario25:
    print(f"el precio del pan es {diccionario25["pan"]}")
else:
    print("producto no disponible")