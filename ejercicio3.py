#3.	Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. 
# Por último, muestra los números ordenados de menor a mayor.

lista= []
i=-1
while i != "0":
    print("Por favor ingrese los numeros a de la lista a organizar.    Para finalizar digite 0")
    numeros=(input())
    i=numeros
    lista.append(numeros)
    
lista.remove('0')
lista.sort()



print(f"los numeros ingresados y organizados de menos a mayor son: {lista}")

 


    
