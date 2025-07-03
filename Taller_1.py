# TALLER DE INTRODUCCION A PYTHON

# PRIMERA PARTE
print("Variables y Strings (1-10)")

# 1. Crea una variable llamada `nombre` y asígnale tu nombre como string.
print("1. Crea una variable llamada `nombre` y asígnale tu nombre como string.")
nombre = input("ingresa tu nombre: ")

# 2. Imprime un saludo personalizado usando la variable `nombre`.
print("\n2. Imprime un saludo personalizado usando la variable `nombre`. ")
saludo = f"hola estudiante {nombre}"
print(saludo)

# 3. Crea una variable `ciudad` con el nombre de tu ciudad.
print("\n3. Crea una variable `ciudad` con el nombre de tu ciudad.")
ciudad = input("ingresa tu ciudad: ")

# 4. Imprime: "Hola, soy [nombre] y vivo en [ciudad]." 
print("\n4. Imprime: Hola, soy [nombre] y vivo en [ciudad].")
hola = f"Hola, soy {nombre} y vivo en {ciudad}"
print(hola)

# 5. Usa `input()` para pedirle al usuario su color favorito y guarda la respuesta en `color`. 
print("\n5. Usa `input()` para pedirle al usuario su color favorito y guarda la respuesta en `color`. ")
color = input(f"{nombre} por favor ingresa tu color favorito: ")

# 6. Imprime un mensaje que diga: "Tu color favorito es [color]." 
print("\n6. Imprime un mensaje que diga: Tu color favorito es [color].")
mensaje_color = f"tu color favorito es {color}"
print(mensaje_color)

# 7. Crea una variable `animal` y asígnale el string "gato". Luego, cambia su valor a "perro".
print("\n7. Crea una variable `animal` y asígnale el string gato. Luego, cambia su valor a perro.")
animal = "gato"
animal = "perro"
print(animal)

# 8. Concatena `nombre` y `ciudad` en una sola variable llamada `presentacion`. 
print("\n8. Concatena `nombre` y `ciudad` en una sola variable llamada `presentacion`.")
presentacion = "soy " + nombre + " y vivo en " + ciudad
print(presentacion)

# 9. Pide 4 datos al usuario, imprime resultado 
print("\n9. Pide 4 datos al usuario, imprime resultado ")
dato1 = input("ingresa tu primer nombre: ")
dato2 = input("ingresa tu segundo nombre: ")
dato3 = input("ingresa tu primer apellido: ")
dato4 = input("ingresa tu segundo apellido: ")
print(dato1, dato2, dato3, dato4)

# 10. Pide 5 datos y has una operacion matematica  
print("\n10. Pide 5 datos y has una operacion matematica ")
nombre2 = input("ingresa tu nombre: ")
pregunta2 = input(f"""ok {nombre2}, deseas hacer una operacion matematica?
               si(presiona 1), no(presiona 2): """)
if pregunta2 == "1":
    n1 = float(input(f"{nombre2} ingresa el primer numero: "))
    n2 = float(input(f"{nombre2} ingresa el segundo numero: "))
    operacion = input("""que operacion matematica desea realizar?
          PRESIONA LA TECLA DE LA OPERACION QUE DESEAS REALIZAR
          suma: (+)
          resta: (-)
          division (/)
          division entera (//)
          multiplicacion (*)
          """)
    
    if operacion == "+":
        suma = n1 + n2
        print(f"la suma es: {suma}")
    elif operacion == "-":
        resta = n1 - n2
        print(f"la resta es: {resta}")
    elif operacion == "/":
        division = n1 / n2
        print(f"la division es: {division}")
    elif operacion == "//":
        division_entera = n1 // n2
        print(f"la division entera es: {division_entera}")
    elif operacion == "*":
        multiplicacion = n1 * n2
        print(f"la multiplicacion es: {multiplicacion}")
    else:
        print(f" esto no es una operacion matematica ({operacion})?")

# SEGUNDA PARTE
print("\nOperaciones Matemáticas con `int` (1120)")

print("\n11. Crea dos variables `a = 5` y `b = 3`, y muestra su suma. ")
a = 5
b = 3
suma1 = a + b
print(suma1)

# 12. Calcula la resta entre `a` y `b`. 
print("\n12. Calcula la resta entre `a` y `b`. ")
resta1 = a - b
print(resta1)

# 13. Multiplica `a` por `b` y guarda el resultado en `multiplicacion`. 
print("\n13. Multiplica `a` por `b` y guarda el resultado en `multiplicacion`. ")
multiplicacion1 = a * b
print(multiplicacion1)

# 14. Divide `a` entre `b` y muestra el resultado (asegúrate de obtener un número decimal). 
print("\n14. Divide `a` entre `b` y muestra el resultado (asegúrate de obtener un número decimal).")
division1 = a / b
print(division1)

# 15. Eleva `a` a la potencia de `b`. 
print("\n15. Eleva `a` a la potencia de `b`. ")
potencia1 = a ** b
print(potencia1)

# 16. Usa `input()` para pedirle al usuario su edad y guárdala como número entero.
print("\n16. Usa `input()` para pedirle al usuario su edad y guárdala como número entero.")
edad = int(input(f"{nombre} ingresa tu edad: "))

# 17. Suma 10 a la edad ingresada y muestra cuántos años tendrá en 10 años. 
print("\n17. Suma 10 a la edad ingresada y muestra cuántos años tendrá en 10 años. ")
edadsuma = edad + 10
print(f"{nombre} en 10 años tendras {edadsuma} años")

# 18. Pide dos números al usuario con `input()` y muestra su suma. 
print("\n18. Pide dos números al usuario con `input()` y muestra su suma. ")
number1 = float(input("ingresa un numero: "))
number2 = float(input("ingresa otro numero: "))
suma10 = number1 + number2
print(f"la suma es {suma10}")

# 19. Calcula el módulo (residuo) de `a % b`. 
print("\n19. Calcula el módulo (residuo) de `a %, b`. ")
residuo = a % b
print(residuo)

# 20. Calcula el promedio de tres números enteros que ingrese el usuario.
print("\n20. Calcula el promedio de tres números enteros que ingrese el usuario.")
numero1 = int(input("ingresa un numero: "))
numero2 = int(input("ingresa otro numero: "))
numero3 = int(input("ingresa otro numero: "))
promedio = (numero1 + numero2 + numero3)/3
print(f"su promedio es {promedio}")

# TERCERA PARTE
print("\nAplicación y Comprensión (21-27) ")

# 21. Pide al usuario su nombre completo y guarda la respuesta en `nombre_completo`.
print("\n21. Pide al usuario su nombre completo y guarda la respuesta en `nombre_completo`.")
nombre_completo = input("ingresa tu nombre completo: ")

# 22. Imprime solo el primer nombre (usa slicing o `.split()`).
print("\n22. Imprime solo el primer nombre (usa slicing o `.split()`).")
primer_nombre = nombre_completo.split()[0]
print("Tu primer nombre es:", primer_nombre)

# 23. Solicita al usuario dos números, luego imprime cuál es mayor. 
print("\n23. Solicita al usuario dos números, luego imprime cuál es mayor. ")
num1 = float(input("ingresa un numero: "))
num2 = float(input("ingresa otro numero: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 < num2:
    print(f"{num2} es mayor que {num1}")
else:
    print("los numeros son iguales :)")

# 24. Pregunta al usuario su año de nacimiento y calcula su edad (usa el año actual manualmente, por ejemplo, 2025). 
print("\n24. Pregunta al usuario su año de nacimiento y calcula su edad (usa el año actual manualmente, por ejemplo, 2025).")
año_de_nacimiento = int(input(f"{nombre} cual es tu año de nacimiento?: "))
edad_calculada1 = 2025 - año_de_nacimiento
edad_calculada2 = 2024 - año_de_nacimiento
print(f"tu edad segun mis calculos es: si ya cumpliste en este año: {edad_calculada1}, si todavia no has cumplido en este año: {edad_calculada2}")

# 25. Crea un mensaje que diga: "Hola [nombre], naciste en [año_nacimiento] y tienes [edad] años." 
print("\n25. Crea un mensaje que diga: Hola [nombre], naciste en [año_nacimiento] y tienes [edad] años. ")
print(f"hola {nombre}, naciste en {año_de_nacimiento} y tienes {edad} años") 
 
# 26. Usa `input()` para preguntar el nombre de una fruta, y responde con: "Me gusta la [fruta]". 
print("\n26. Usa `input()` para preguntar el nombre de una fruta, y responde con: Me gusta la [fruta]. ")
fruta = input(f"{nombre} dame el nombre de una fruta: ")
print(f"me gusta la {fruta} :)")

# 27. Pide dos números, muestra la suma, resta, multiplicación y división en un mismo bloque.
print("\n27. Pide dos números, muestra la suma, resta, multiplicación y división en un mismo bloque.")
pedir_numero1 = float(input("ingresa un numero: "))
pedir_numero2 = float(input("ingresa otro numero: "))

suma100 = pedir_numero1 + pedir_numero2
resta100 = pedir_numero1 - pedir_numero2
multiplicacion100 = pedir_numero1 * pedir_numero2

if pedir_numero2 != 0:
    division100 = pedir_numero1 / pedir_numero2
else:
    division100 = "No se puede dividir entre cero"

print(f"""
Resultados:     
Suma: {suma100}
Resta: {resta100}
Multiplicación: {multiplicacion100}
División: {division100}
""")