

numEmployees = 0
name = ""
nameBad = ""
nameBest = ""
baseSal = 0
extraHours = 0
catEmplo = ""
valExtraH = 0
totalSal = 0
bestSal = 0
badSal = 0
totalPayroll = 0
i = 0

numEmployees = int(input("Ingrese cantidad de empleados: "))

for i in range (i,int(numEmployees)):


    name = input("Ingrese el nombre del empleado: ")

    baseSal = int(input("Ingrese el salario basico del empleado: "))

    extraHours = int(input("Ingrese la cantidad de horas extras del empleado: "))

    if baseSal > 600000:
        catEmplo = "B"
    elif baseSal >= 200000:
        catEmplo = "A"

    
    valExtraH = (baseSal * 0.10)*extraHours
    
    totalSal = baseSal + valExtraH
    totalPayroll = totalPayroll+totalSal

    if bestSal < totalSal:
        bestSal = totalSal
        nameBest = name
    elif badSal < totalSal:
        badSal = totalSal
        nameBad = name

    

    print("El empleado: "+name+", tiene un salario de "+str(baseSal)+", tiene un extra de horas extras de "+str(valExtraH)+", pertenece a la categoria "+catEmplo+", y el sueldo total es de "+str(totalSal))

    

print("El empleado que mejor salario tiene es "+nameBest+", con salario de "+str(bestSal)+", y el que menor salario tiene es "+nameBad+", con un salario de "+str(badSal))
print("el valor total que debe pagar la empresa por concepto de nómina es de: "+str(totalPayroll))