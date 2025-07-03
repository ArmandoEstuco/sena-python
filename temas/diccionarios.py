persona1 = {
    "nombre": "carlos",
    "edad": 30,
    "profesion": "ingeniero"
}

persona2 = {
    "nombre": "alberto",
    "edad": 2,
    "nacimiento": "palmira",
    "telefono": "324580000",
    "profesion": "comunicador",
    "cc": (123456789)
}


auto = {
    "marca": "ford",
    "modelo": "mustang",
    "año": 2022,
    "placa": ("ABC123")
}

# imprimir algo del diccionario
print(auto["modelo"])

# modificar un valor
auto["año"] = 2023

# eliminar con (del)
del auto["modelo"]

# eliminar con (pop)
auto.pop("placa")

# el (del) y el .pop() lanza key error si voy a eliminar un elemento que no existe
#del auto["nose"] # keyError
#auto.pop("nose") # keyError
print(auto)

# el .pop() puede devolver un valor
