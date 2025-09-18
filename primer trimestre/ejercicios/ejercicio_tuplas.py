# ejercicio 1

frutas = ("manzana", "pera")
lista_frutas = list(frutas)
lista_frutas.append(input("ingresa otra fruta: "))
frutas_final = tuple(lista_frutas)

print(f"tupla final: {frutas_final}")

# ejercicio 2

calificaciones = (4.2, 3.8)
lista_calificaciones = list(calificaciones)
lista_calificaciones.append(input("ingresa otra calificacion: "))
calificaciones_final = tuple(lista_calificaciones)

print(f"tupla final: {calificaciones_final}")

# ejercicio 3

datos_personales = ("ana", "gomez")
lista_datos = list(datos_personales)
lista_datos.append(input("ingresa tu numero de documento: "))
datos_finales = tuple(lista_datos)

print(f"tupla final: {datos_finales}")
