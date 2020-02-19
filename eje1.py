edad =""
promEdad = 0
contE = 0
auxEdad  = 0
iterador = True

while(iterador){
    edad = input("Ingrese la edad")

    if(edad>18){
        promEdad= contE / auxEdad
        print("El promedio de edad es de: "+promEdad)
    }

    contE+=1

    iterador = input("Desea seguir ejecutando el programa? aceptar para continuar, cancelar para terminar")    

}