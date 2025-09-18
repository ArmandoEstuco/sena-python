# lista para guardar los datos
personas = []

# preguntar cuántas personas registrar con un maximo de 5 personas
cantidad = int(input("¿Cuántas personas desea registrar? (máximo 5): "))
if cantidad > 5:
# si se ingresa un numero mayor a 5, se ajusta a 5
    cantidad = 5

# persona 1
if cantidad >= 1:
    nombre = input("Nombre persona 1: ")
    peso = float(input("Peso en kg: "))
    estatura = float(input("Estatura en m: "))
    imc = peso / (estatura * estatura)
    if imc < 18.5:
        estado = "Bajo peso"
    elif imc < 25:
        estado = "Peso normal"
    elif imc < 30:
        estado = "Sobrepeso"
    else:
        estado = "Obesidad"
    personas.append({"nombre": nombre, "imc": imc, "estado": estado})

# persona 2
if cantidad >= 2:
    nombre = input("Nombre persona 2: ")
    peso = float(input("Peso en kg: "))
    estatura = float(input("Estatura en m: "))
    imc = peso / (estatura * estatura)
    if imc < 18.5:
        estado = "Bajo peso"
    elif imc < 25:
        estado = "Peso normal"
    elif imc < 30:
        estado = "Sobrepeso"
    else:
        estado = "Obesidad"
    personas.append({"nombre": nombre, "imc": imc, "estado": estado})

# persona 3
if cantidad >= 3:
    nombre = input("nombre persona 3: ")
    peso = float(input("peso en kg: "))
    estatura = float(input("estatura en m: "))
    imc = peso / (estatura * estatura)
    if imc < 18.5:
        estado = "Bajo peso"
    elif imc < 25:
        estado = "Peso normal"
    elif imc < 30:
        estado = "Sobrepeso"
    else:
        estado = "Obesidad"
    personas.append({"nombre": nombre, "imc": imc, "estado": estado})

# persona 4
if cantidad >= 4:
    nombre = input("Nombre persona 4: ")
    peso = float(input("Peso en kg: "))
    estatura = float(input("Estatura en m: "))
    imc = peso / (estatura * estatura)
    if imc < 18.5:
        estado = "Bajo peso"
    elif imc < 25:
        estado = "Peso normal"
    elif imc < 30:
        estado = "Sobrepeso"
    else:
        estado = "Obesidad"
    personas.append({"nombre": nombre, "imc": imc, "estado": estado})

# persona 5
if cantidad == 5:
    nombre = input("Nombre persona 5: ")
    peso = float(input("Peso en kg: "))
    estatura = float(input("Estatura en m: "))
    imc = peso / (estatura * estatura)
    if imc < 18.5:
        estado = "Bajo peso"
    elif imc < 25:
        estado = "Peso normal"
    elif imc < 30:
        estado = "Sobrepeso"
    else:
        estado = "Obesidad"
    personas.append({"nombre": nombre, "imc": imc, "estado": estado})

# mostrar resumen
print("\nResumen de personas registradas:")
if cantidad == 0:
    print("No se registraron personas.")
if cantidad >= 1:
    print(f"{personas[0]['nombre']} - IMC: {personas[0]['imc']:.2f} - Estado: {personas[0]['estado']}")
if cantidad >= 2:
    print(f"{personas[1]['nombre']} - IMC: {personas[1]['imc']:.2f} - Estado: {personas[1]['estado']}")
if cantidad >= 3:
    print(f"{personas[2]['nombre']} - IMC: {personas[2]['imc']:.2f} - Estado: {personas[2]['estado']}")
if cantidad >= 4:
    print(f"{personas[3]['nombre']} - IMC: {personas[3]['imc']:.2f} - Estado: {personas[3]['estado']}")
if cantidad == 5:
    print(f"{personas[4]['nombre']} - IMC: {personas[4]['imc']:.2f} - Estado: {personas[4]['estado']}")
