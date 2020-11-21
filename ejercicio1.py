# 1.	Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de
#  apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace hoy"
# debe devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1


def separar(cadena):

    nueva_cadena = cadena.replace(".", "")
    nueva_cadena = nueva_cadena.replace(",", "")
    nueva_cadena = nueva_cadena.replace("-", "")
    nueva_cadena = nueva_cadena.replace("?", "")

    nueva_cadena = nueva_cadena.lower()


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

print(f"la lista de palabras, con la cantidad de veces que se repite es:{resultado}")
