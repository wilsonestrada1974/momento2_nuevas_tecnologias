#4.	Hacer una actividad que pida al usuario escribir una cantidad X 
# de nombres de personas (puede hacerlo con el ciclo que considere). 
# Después el sistema deberá demostrar cuales son los nombres que 
# empiezan con la letra "C" sea minúscula o mayúscula.

lista=[]
lista1=[]
nombres={}
iterador=1
dato=[]
letra=1

while iterador != "0":
    print("Por favor ingrese los nombres.   Para terminar digite 0")
    nombre=input()
    iterador=nombre
    nombre.lower()
    nuevo=nombre.replace("", " ")
    lista.append(nombre)
    otro=nuevo.split(" ")
    if otro[1] == 'c':
        lista1.append(nombre)
    

lista.remove('0')
print(f"La lista total de los nombres ingresados es: {lista}")
print(f"La lista de los nombres que comienzan con la letra C es: {lista1}")






