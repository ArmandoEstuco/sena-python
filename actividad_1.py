lista1 = ["hola", "no se", "a"] 
lista2 = [1, 2, 3, "a"] 

lista1.append(100)
lista1.append("hola mundo")

lista2.append("hola y adios")
lista2.append(300)

lista3 = lista1.copy()
lista3.pop() 

lista4 = lista2.copy()
lista4.remove("hola y adios") 
lista4.pop() 

lista5 = []
lista5.extend(lista4)
lista5.extend(lista3)