
numero = 0
numMen = 0
aux = 0

for i in range(1,3):
    
    numero = input("Ingrese la el numero a evaluar de 0 a 10.000: ")

    for j in range(len(numero)):
        if numero[i] < numero[j+1]:
            aux=numero[i]
    


print("El numero menor: "+str(numMen)+", de el numero ingresado es: "+numero)
