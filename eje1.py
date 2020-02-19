edad =""
promEdad = 0
contE = 0
auxEdad  = 0
iterador = "1"

while iterador == "1":
    edad = int(input("Ingrese la edad: "))
    auxEdad += edad

    if edad > 18:
        promEdad =  (auxEdad-edad )/ contE
        print("El promedio de edad es de: "+str(promEdad))
    

    contE+=1

    iterador = input("Desea seguir ejecutando el programa? 1 para continuar, 2 para terminar: ")

promEdad = auxEdad / contE

print("El promedio de edad es de: "+str(promEdad))