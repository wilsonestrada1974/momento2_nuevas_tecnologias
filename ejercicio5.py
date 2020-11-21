#5.	Realice una FUNCIÓN en Python que calcule el índice de masa corporal 
# de una persona y diga el estado en que se encuentre. Debe recibir los parámetros necesarios.

def masa (peso, talla):
    indice=peso/(talla*talla)

    print("su indice de masa corporal es de: ","{:.2f}".format(indice))
    if indice <= 18.5:
        print("Su peso es insuficiente")
    elif indice > 18.5 and indice <= 24.9 :
        print("Su peso es normal")
    elif indice > 24.9 and indice <= 26.9:
        print("Usted tiene sobrepeso grado 1")
    elif indice > 26.9 and indice <= 29.9:
        print ("Usted tiene sobrepeso grado II (Preobesidad)")
    elif indice > 29.9 and indice <=34.9:
        print ("Usted tiene obesidad tipo I")
    elif indice > 34.9 and indice <= 39.9:
        print("Usted oadece de obesidad tipo II")
    elif indice > 39.9 and indice <= 49.9:
        print("Usted padece de obesidad tipo III (Morbida)")
    elif indice >49.9:
        print("usted padece de obesidad tipo IV (Obesidad Extrema")        


print("Por favor Ingrese su Peso en Kilogramos")
peso=float(input())
print("Por favor ingrese su talla en metros")
talla=float(input())

masa(peso, talla)

