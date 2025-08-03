'''
vocal = input("ingrese una vocal:")
if vocal in "aeiou": print(vocal.upper())
elif vocal in "AEIOU": print(vocal.lower())
else: print("no es una vocal")
'''
# 2 lineas? 

vocal = input("ingrese una vocal:")
print(vocal.upper() if vocal in "aeiou" else vocal.lower() if vocal in "AEIOU" else "no es una vocal")