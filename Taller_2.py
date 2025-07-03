'''
# 1. Calculadora de promedio
calificaciones = []
calificaciones.append(float(input("ingresa la calificacion: ")))
calificaciones.append(float(input("ingresa la calificacion: ")))
calificaciones.append(float(input("ingresa la calificacion: ")))

promedio = sum(calificaciones) / len(calificaciones)
print(f'el promedio es: {promedio}')

# 2. Actualiza precios
productos = {
    'pan': 1200,
    'arepa': 3000,
    'papa': 5000
}
print(productos)
porcentaje = float(input('ingresa el porcentaje de aumento: '))
productos["pan"] += productos["pan"] * (porcentaje / 100)
productos["arepa"] += productos["arepa"] * (porcentaje / 100)
productos["papa"] += productos["papa"] * (porcentaje / 100)

print(f'nuevos precios: {productos}')

# 3. conversor de temperaturas
t1 = float(input('temperatura del día 1 en celsius: '))
t2 = float(input('temperatura del día 2 en celsius: '))
t3 = float(input('temperatura del día 3 en celsius: '))
t4 = float(input('temperatura del día 4 en celsius: '))
t5 = float(input('temperatura del día 5 en celsius: '))
temperaturas_celcius = (t1, t2, t3, t4, t5)

f1 = t1 * 9/5 + 32
f2 = t2 * 9/5 + 32
f3 = t3 * 9/5 + 32
f4 = t4 * 9/5 + 32
f5 = t5 * 9/5 + 32
temperaturas_fahrenheit = (f1, f2, f3, f4, f5)
print(f"temperaturas en celcius: {temperaturas_celcius}")
print(f"temperaturas en fahrenheit: {temperaturas_fahrenheit}")

# 4. Edad promedio con listas
edades = [int(input('edad 1: ')), int(input('edad 2: ')), int(input('edad 3: ')), int(input('edad 4: ')), int(input('edad 5: '))]

promedio = sum(edades) / len(edades)

print(f'mayor: {max(edades)}, menor: {min(edades)}, promedio: {promedio}')

# 5. Diccionario de frutas
frutas = {
    "manzana": 3000,
    "pera": 2500,
    "banano": 1500
}
kilos_manzana = float(input("kilos de manzana: "))
kilos_pera = float(input("kilos de pera: "))
kilos_banano = float(input("kilos de banano: "))

total = frutas["manzana"] * kilos_manzana + frutas["pera"] * kilos_pera + frutas["banano"] * kilos_banano
print(f'el total a pagar es: {total}')

# 6. Suma de elementos en tupla
tupla_numeros = (1, 2, 3, 4, 5)
suma_tupla_numeros = sum(tupla_numeros)
print(suma_tupla_numeros)

# 7. Inventario con lista de diccionarios
producto1 = {
    "nombre": input("ingrese el nombre del primer producto: "),
    "cantidad": int(input("ingrese la cantidad del primer producto: ")),
    "precio": float(input("ingrese el precio del primer producto: "))
}

producto2 = {
    "nombre": input("ingrese el nombre del segundo producto: "),
    "cantidad": int(input("ingrese la cantidad del segundo producto: ")),
    "precio": float(input("ingrese el precio del segundo producto: "))
}

producto3 = {
    "nombre": input("ingrese el nombre del tercer producto: "),
    "cantidad": int(input("ingrese la cantidad del tercer producto: ")),
    "precio": float(input("ingrese el precio del tercer producto: "))
}

productos = [producto1, producto2, producto3]

total1 = producto1["cantidad"] * producto1["precio"]
total2 = producto2["cantidad"] * producto2["precio"]
total3 = producto3["cantidad"] * producto3["precio"]

total_inventario = total1 + total2 + total3

print(f"\nEl total del inventario es: ${total_inventario:.2f}")

# 8. Modificar una lista de precios
lista_precios = [
    200000,
    100000,
    50000,
    20000,
    10000
]
print(f"precios:\n${lista_precios[0]}, ${lista_precios[1]}, ${lista_precios[2]}, ${lista_precios[3]}, ${lista_precios[4]},")

descuento = float(input("ingresa un descuento en porcenaje para esos productos: "))
precio1 = lista_precios[0] - (lista_precios[0] * descuento / 100) 
precio2 = lista_precios[1] - (lista_precios[1] * descuento / 100) 
precio3 = lista_precios[2] - (lista_precios[2] * descuento / 100) 
precio4 = lista_precios[3] - (lista_precios[3] * descuento / 100) 
precio5 = lista_precios[4] - (lista_precios[4] * descuento / 100) 

print(f"los nuevos precios son:\n{precio1}\n{precio2}\n{precio3}\n{precio4}\n{precio5}")

# 9. Notas con tuplas
nota1 = float(input("ingresa la primera nota para la tupla: "))
nota2 = float(input("ingresa la segunda nota para la tupla: "))
nota3 = float(input("ingresa la tercera nota para la tupla: "))
nota4 = float(input("ingresa la cuarta nota para la tupla: "))

tupla_notas = (
    nota1,
    nota2,
    nota3,
    nota4
)

print(f"mayor: {max(tupla_notas)}, menor: {min(tupla_notas)}")

# 10.  Diccionario de conversiones
conversiones = {
    "kilometro": 1000,
    "metro": 1,
    "centimetro": 0.01,
}

def volver():
    convertir_otra = input("deseas convertir otra unidad?: ")
    if convertir_otra == "si":
        print("OK")
        proceso_conversiones()
    elif convertir_otra == "no":
        print("OK")
    else:
        print("ESTO NO ES UNA OPCION VALIDA!")
        volver()

def proceso_conversiones():
    unidad = input(f"que unidad deseas convertir a metros: km, m, cm\n:")

    if unidad == "km":
        cantidad1 = float(input(f"ingresa la cantidad de kilometros para convertir a metros: "))
        conversion1 = cantidad1 * conversiones["kilometro"]
        print(f"{cantidad1}km en metros son {conversion1}m")
        volver()
    elif unidad == "m":
        cantidad2 = float(input(f"ingresa la cantidad de metros para convertir a metros: "))
        conversion2 = cantidad2 * conversiones["metro"]
        print(f"{cantidad2}m en metros son {conversion2}m")
        volver()
    elif unidad == "km":
        cantidad3 = float(input(f"ingresa la cantidad de centimetros para convertir a metros: "))
        conversion3 = cantidad3 * conversiones["centimetro"]
        print(f"{cantidad3}cm en metros son {conversion3}m")
        volver()
    else:
        print("ESTO NO ES UNA OPCION EN EL DICCIONARIO!")
        proceso_conversiones()
        
proceso_conversiones()

# 11. Pide al usuario una lista de precios. Luego crea una nueva lista con el precio más el 19% de IVA. 
price1 = float(input("precio 1: "))
price2 = float(input("precio 2: "))
price3 = float(input("precio 3: "))
price4 = float(input("precio 4: "))
price5 = float(input("precio 5: "))
precios1 = [price1, price2, price3, price4, price5]
iva = [price1 * 1.19, price2 * 1.19, price3 * 1.19, price4 * 1.19, price5 * 1.19]
print(iva)

# 12. Pide al usuario dos números. Guarda en una tupla la suma, resta, multiplicación y división entre ellos. 
operacion1 = float(input("numero 1: "))
operacion2 = float(input("numero 2: "))
operaciones1 = (operacion1 + operacion2, operacion1 - operacion2, operacion1 * operacion2, operacion1 / operacion2)
print(operaciones1)

# 13. Crea un diccionario donde las claves sean nombres de estudiantes y los valores sus notas. Calcula el promedio general.
notas1 = {
    "ana": float(input("nota de alberto: ")),
    "juan": float(input("nota de elbazurita: ")),
    "luisa": float(input("nota de kein_becil: "))
}
promedio1 = (notas1["alberto"] + notas1["elbazurita"] + notas1["kein_becil"]) / 3
print(f"promedio general: {promedio1}")

# 14. Pide al usuario cinco salarios. Aplícales un aumento del 10% y guarda los nuevos valores en otra lista. 
salario1 = float(input("salario 1: "))
salario2 = float(input("salario 2: "))
salario3 = float(input("salario 3: "))
salario4 = float(input("salario 4: "))
salario5 = float(input("salario 5: "))
salarios = [salario1, salario2, salario3, salario4, salario5]
nuevos_salarios = [salario1*1.1, salario2*1.1, salario3*1.1, salario4*1.1, salario5*1.1]
print(salarios)
print(nuevos_salarios)

# 15. Guarda productos con su precio sin impuesto. Pide al usuario el porcentaje de impuesto y calcula el precio final para cada uno. 
productos = {
    "redmagic": 8000000, 
    "pc_gamer": 800000, 
    "death_note": 600000
}
impuestos = float(input("porcentaje de impuesto: "))
f = 1 + impuestos / 100
con_impuestos = {
    "redmagic": productos["redmagic"] * f,
    "pc_gamer": productos["pc_gamer"] * f,
    "death_note": productos["death_note"] * f
}
print(con_impuestos)

# 16. Solicita al usuario una lista de edades. Luego indica cuántos son mayores de edad y cuántos no. 
edad1 = int(input("edad 1: "))
edad2 = int(input("edad 2: "))
edad3 = int(input("edad 3: "))
edad4 = int(input("edad 4: "))
edad5 = int(input("edad 5: "))
edades = [edad1, edad2, edad3, edad4, edad5]
mayores1 = int(edad1 >= 18) + int(edad2 >= 18) + int(edad3 >= 18) + int(edad4 >= 18) + int(edad5 >= 18)
menores1 = 5 - mayores1
print(f"mayores: {mayores1}, menores: {menores1}")

# 17. Crea una tupla con los valores de una cantidad en dólares convertida a euros, pesos y yenes, usando tasas fijas.
dolares = float(input("monto en dolares: "))
conversiones1 = (dolares * 0.9, dolares * 4000, dolares * 150)
print(f"euros, pesos, yenes: {conversiones1}")

# 18. Pide al usuario registrar la venta de tres productos (nombre y cantidad). Luego muestra el total de unidades vendidas. 
venta_producto1 = {
    "nombre": input("producto 1: "), 
    "cantidad": int(input("cantidad 1: "))
}
venta_producto2 = {
    "nombre": input("producto 2: "), 
    "cantidad": int(input("cantidad 2: "))
}
venta_producto3 = {
    "nombre": input("producto 3: "), 
    "cantidad": int(input("cantidad 3: "))
}
total_venta_producto = venta_producto1["cantidad"] + venta_producto2["cantidad"] + venta_producto3["cantidad"]
print(f"total vendido: {total_venta_producto}")

# 19. Crea una lista con diez temperaturas. Muestra cuáles superan los 30 grados y cuáles están por debajo de 10. 
def analizar(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10):
    altas = []
    bajas = []

    if t1 > 30:
        altas.append(t1)
    elif t1 < 10:
        bajas.append(t1)

    if t2 > 30:
        altas.append(t2)
    elif t2 < 10:
        bajas.append(t2)

    if t3 > 30:
        altas.append(t3)
    elif t3 < 10:
        bajas.append(t3)

    if t4 > 30:
        altas.append(t4)
    elif t4 < 10:
        bajas.append(t4)

    if t5 > 30:
        altas.append(t5)
    elif t5 < 10:
        bajas.append(t5)

    if t6 > 30:
        altas.append(t6)
    elif t6 < 10:
        bajas.append(t6)

    if t7 > 30:
        altas.append(t7)
    elif t7 < 10:
        bajas.append(t7)

    if t8 > 30:
        altas.append(t8)
    elif t8 < 10:
        bajas.append(t8)

    if t9 > 30:
        altas.append(t9)
    elif t9 < 10:
        bajas.append(t9)

    if t10 > 30:
        altas.append(t10)
    elif t10 < 10:
        bajas.append(t10)

    print(f"altas: {altas}")
    print(f"bajas: {bajas}")

temperaturas = [9, 13, 6, 34, 21, 33, 2, 27, 12, 47]
analizar(
    temperaturas[0], temperaturas[1], temperaturas[2], temperaturas[3], temperaturas[4],
    temperaturas[5], temperaturas[6], temperaturas[7], temperaturas[8], temperaturas[9]
)
'''
# 20. Crea una lista con cinco precios. Permite que el usuario elimine uno, agregue otro, y luego muestra la lista ordenada de menor a mayor.
cinco_precios = [3000, 5000, 1000, 4000, 2000]
print(cinco_precios)

accion1 = input("quieres hacer algo con esos precios? (si/no): ")

def eliminar_precio():
    global cinco_precios
    eliminar = float(input("que precio vas a eliminar: "))
    if eliminar in cinco_precios:
        cinco_precios.remove(eliminar)
        print(f"se elimino {eliminar}")
    else:
        print("ese precio no está en la lista")

def agregar_precio():
    global cinco_precios
    try:
        agregar = float(input("precio a agregar: "))
        cinco_precios.append(agregar)
        print(f"se agrego {agregar}")
    except:
        print("solo se pueden agregar números")
        agregar_precio()

def algo_mas():
    algo_mas = input("deseas hacer algo mas?(si/no)")
    if algo_mas == "si":
        modificar_precio()
    elif algo_mas =="no":
        print("ok")
    else:
        print("opcion no valida")
         
def modificar_precio():
    if accion1 == "si":
        accion2 = input("que quieres hacer?\neliminar?(1)\nagregar?(2)\n:")
        if accion2 == "1":
            eliminar_precio()
            algo_mas()
        elif accion2 == "2":
            agregar_precio()
            algo_mas()
        else:
            print("opcion no valida")

modificar_precio()

ordenado = sorted(cinco_precios)
print(f"lista final ordenada: {ordenado}")