
# 1. edad y categoría
edad = int(input("ingresa tu edad: "))
if edad < 18:
    print('menor de edad')
elif edad < 65:
    print('eres mayor de edad')
else:
    print('eres adulto mayor')

# 2. estatura
estatura = float(input('ingresa tu estatura en metros: '))
if estatura < 1.5:
    print('eres bajo')
elif estatura <= 1.8:
    print('tienes estatura media')
else:
    print('eres alto')

# 3. múltiplos
n = int(input('ingresa un número: '))
if n % 2 == 0:
    print('es múltiplo de 2')
elif n % 3 == 0:
    print('es múltiplo de 3')
else:
    print('no es múltiplo de 2 ni de 3')

# 4. cantidad de decimales
n = input('ingresa un número decimal: ')
parte_decimal = n.split('.')[-1]
if len(parte_decimal) == 1:
    print('tiene 1 decimal')
elif len(parte_decimal) == 2:
    print('tiene 2 decimales')
else:
    print('tiene más de 2 decimales')

# 5. país en tupla
pais = input('ingresa un país: ')
tupla = ('colombia', 'perú', 'argentina', 'méxico')
if pais.lower() in tupla:
    print('el país está en la lista')
else:
    print('el país no está en la lista')

# 6. tipo de sangre
tipo = input('ingresa tu tipo de sangre: ').upper()
compatibilidad = {
    'A': 'A y AB',
    'B': 'B y AB',
    'AB': 'AB',
    'O': 'todos los tipos'
}
print(f'puedes donar a: {compatibilidad.get(tipo, "tipo desconocido")}')

# 7. temperatura
temp = float(input('ingresa la temperatura en °c: '))
if temp < 10:
    print('hace frío')
elif temp <= 25:
    print('está templado')
else:
    print('hace calor')

# 8. menú de operaciones
op = input('elige opción: 1. sumar 2. restar 3. multiplicar: ')
a = float(input('primer número: '))
b = float(input('segundo número: '))
if op == '1':
    print(f'resultado: {a + b}')
elif op == '2':
    print(f'resultado: {a - b}')
elif op == '3':
    print(f'resultado: {a * b}')
else:
    print('opción inválida')

# 9. número a mes
mes = int(input('ingresa un número del 1 al 12: '))
meses = {
    1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril',
    5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto',
    9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
}
print(f'mes: {meses.get(mes, "inválido")}')

# 10. empieza con
numero = input('ingresa un número de 4 dígitos: ')
if numero.startswith('1'):
    print('comienza con 1')
elif numero.startswith('2'):
    print('comienza con 2')
else:
    print('comienza con otro número')

# 11. primera letra
palabra = input('ingresa una palabra: ')
letra = palabra[0]
if letra.isdigit():
    print('comienza con un número')
elif letra.lower() in 'aeiou':
    print('comienza con una vocal')
else:
    print('comienza con una consonante')

# 12. fruta y precio
fruta = input('ingresa una fruta: ')
lista = ['manzana', 'pera', 'piña']
precios = {'manzana': 3000, 'pera': 2500, 'piña': 2000}
if fruta.lower() in lista:
    print(f'el precio es: {precios[fruta.lower()]}')
else:
    print('fruta no disponible')

# 13. calificación
nota = float(input('ingresa tu calificación (0 a 5): '))
if nota < 3:
    print('reprobado')
elif nota <= 4:
    print('aprobado')
else:
    print('excelente')

# 14. divisibilidad
n = int(input('ingresa un número: '))
if n % 4 == 0:
    print('es divisible entre 4')
elif n % 6 == 0:
    print('es divisible entre 6')
else:
    print('no es divisible ni entre 4 ni entre 6')

# 15. autenticación
usuario = input('usuario: ')
clave = input('clave: ')
usuarios = {'juan': '1234', 'ana': 'abcd'}
if usuario in usuarios and clave == usuarios[usuario]:
    print('acceso permitido')
else:
    print('acceso denegado')

# 16. grupo por edad
edad = int(input('ingresa tu edad: '))
if edad <= 12:
    print('niño')
elif edad <= 17:
    print('adolescente')
elif edad <= 64:
    print('adulto')
else:
    print('mayor')

# 17. capital o secundaria
ciudad = input('ingresa el nombre de una ciudad: ')
capitales = ('bogotá', 'lima', 'buenos aires', 'ciudad de méxico')
if ciudad.lower() in capitales:
    print('es una capital')
else:
    print('ciudad secundaria')

# 18. descuento por compra
valor = float(input('ingresa el valor de la compra: '))
if valor > 200000:
    total = valor * 0.85
elif valor >= 100000:
    total = valor * 0.90
else:
    total = valor
print(f'valor final: {total}')

# 19. salario con bono
nombre = input('nombre del trabajador: ')
horas = float(input('horas trabajadas: '))
tarifa = 10000
salario = horas * tarifa
if horas > 40:
    salario *= 1.20
print(f'{nombre}, tu salario es: {salario}')

# 20. puntaje de prueba
puntaje = int(input('ingresa tu puntaje (0 a 100): '))
if puntaje < 50:
    print('insuficiente')
elif puntaje < 80:
    print('aceptable')
else:
    print('sobresaliente')
