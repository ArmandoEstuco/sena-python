#'''
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

print(f"{tupla_notas}")

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
#'''