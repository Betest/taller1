edad =""
promEdad = 0
contE = 0
auxEdad  = 0
iterador = "1"

while iterador == "1":
    edad = int(input("Ingrese la edad: "))
    auxEdad += edad

    if edad > 18 :
        if contE > 0:
            promEdad =  (auxEdad-edad )/ contE
        print("El promedio de edad es de: "+str(promEdad))
        break       
    

    contE+=1

    iterador = input("Desea seguir ejecutando el programa? 1 para continuar, 2 para terminar: ")

if contE > 0:
    promEdad = auxEdad / contE

print("El promedio de edad es de: "+str(promEdad))