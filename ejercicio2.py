#2.	Escribir una función que cuente la cantidad de apariciones 
# de cada carácter en una cadena de texto, y los devuelva en un diccionario.

def separar(cadena):

    nueva_cadena = cadena.replace("", " ")
    
    lista = nueva_cadena.split()

    lista_palabras = dict()

    for palabra in lista:
        lista_palabras[palabra] = lista_palabras.get(palabra, 0) + 1

        nombre_palabra = lista[0]
        cantidad_palabra = 0

    return lista_palabras



print("por favor ingrese la cadena a evaluar")
datos = input()

resultado = separar(datos)

print(f"la lista de caracteres, con la cantidad de veces que se repite es:{resultado}")