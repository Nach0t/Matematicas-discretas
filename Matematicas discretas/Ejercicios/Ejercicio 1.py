#Calculador de año bisiesto
def calcular_año(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print("Es bisiesto")
    else:
        print("No es bisiesto")

año = int(input("Ingrese un año: "))

print(calcular_año(año))
