
numero = input("Ingrese la cantidad de numeros de la succesion de Fibonacci: ")
aux = 0
aux2 = 1

for num in range(1,int(numero)):

    print("Numero Fibonacci: "+str(aux))
    aux3=aux+aux2
    aux=aux2
    aux2=aux3
    
    
    
    