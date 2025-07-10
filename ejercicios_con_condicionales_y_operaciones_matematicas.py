# 1
num1 = int(input("ingresar numero: "))
if num1 > 0:
    print(f"{num1} es positivo")
elif num1 < 0:
    print(f"{num1} es negativo")
else:
    print(f"{num1} es cero")

# 2
num2a = int(input("ingresar primer numero: "))
num2b = int(input("ingresar segundo numero: "))
if num2a > num2b:
    print(f"el mayor es {num2a}")
elif num2b > num2a:
    print(f"el mayor es {num2b}")
else:
    print("los dos numeros son iguales")

# 3
num3 = int(input("ingresar numero: "))
if num3 % 2 == 0:
    print(f"{num3} es par")
else:
    print(f"{num3} es impar")

# 4
num4 = int(input("ingresar numero: "))
if num4 >= 10 and num4 <= 20:
    print(f"{num4} esta entre 10 y 20")
else:
    print(f"{num4} no esta entre 10 y 20")

# 5
num5a = int(input("ingresar primer número: "))
num5b = int(input("ingresar segundo número: "))
num5c = int(input("ingresar tercer número: "))
if num5a >= num5b and num5a >= num5c:
    print(f"el mayor es {num5a}")
elif num5b >= num5a and num5b >= num5c:
    print(f"el mayor es {num5b}")
else:
    print(f"el mayor es {num5c}")

# 6
total6 = float(input("ingresar total: "))
if total6 > 100:
    total6 = total6 * 0.9
print(f"el precio final es ${total6:.2f}")

# 7
edad7 = int(input("ingresar edad: "))
if edad7 >= 18:
    print("puede votar")
else:
    print("no puede votar")

# 8
precio8 = float(input("ingresar precio: "))
cliente8 = input("ingresar tipo cliente (vip o normal): ")
if cliente8.lower() == "vip":
    precio8 = precio8 * 0.8
print(f"precio final ${precio8:.2f}")

# 9
num9 = int(input("ingresar numero: "))
if num9 % 5 == 0 and num9 % 3 == 0:
    print(f"{num9} es multiplo de 5 y 3")
else:
    print(f"{num9} no es multiplo de 5 y 3")

# 10
num10 = int(input("ingresar numero a verificar: "))
div10a = int(input("ingresar primer divisor: "))
div10b = int(input("ingresar segundo divisor: "))
if div10a != 0 and div10b != 0 and num10 % div10a == 0 and num10 % div10b == 0:
    print(f"{num10} es divisible entre {div10a} y {div10b}")
else:
    print(f"{num10} no es divisible entre {div10a} y {div10b}")

# 11
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

# 12
lista12 = [3, 5, 7, 9]
if 7 in lista12:
    print("esta en lista")
else:
    print("no esta en lista")

# 13
lista13 = [4, 6, 2, 8]
suma13 = lista13[0] + lista13[1]
if suma13 > 10:
    print(f"la suma es {suma13} y es mayor a 10")
else:
    print(f"la suma es {suma13} y no es mayor a 10")


