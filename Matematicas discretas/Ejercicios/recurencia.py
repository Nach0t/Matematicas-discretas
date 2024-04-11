import cmath

# Entrada del número de términos en la función de recurrencia
funcion = int(input("Ingrese el número de funciones que hay: "))

lista = []

# Captura de coeficientes de cada término de la recurrencia
for i in range(1, funcion + 1):
    a = input(f"Ingrese el valor que multiplica f(n-{i}): ")
    lista.append(a)

# Creación de la representación de la recurrencia
output = "f(n) = "
for i in range(funcion):
    coeficiente = int(lista[i])
    if coeficiente >= 0:
        if i > 0:  # Añade un '+' solo si no es el primer término
            output += f"+ {coeficiente}f(n-{i+1}) "
        else:
            output += f"{coeficiente}f(n-{i+1}) "
    else:
        output += f"- {abs(coeficiente)}f(n-{i+1}) "

while True:
    # Entrada del símbolo para la solución de EDO
    simbolo = input("Ingrese el símbolo de la ecuación: ")
    if simbolo.lower() != "c":  # Convierte a minúsculas para comparar y salir si es diferente de "c"
        break
    else:
        print("El símbolo 'C' o 'c' no es válido. Por favor, ingrese otro símbolo.")

# Representación de la EDO utilizando el símbolo ingresado
output = f"{simbolo}^n = "
for i in range(funcion):
    coeficiente = int(lista[i])
    if coeficiente >= 0:
        if i > 0:  # Añade un '+' solo si no es el primer término
            output += f"+ {coeficiente}{simbolo}^(n-{i+1}) "
        else:
            output += f"{coeficiente}{simbolo}^(n-{i+1}) "
    else:
        output += f"- {abs(coeficiente)}{simbolo}^(n-{i+1})"

print(output)
print(f"Se multiplica por {simbolo}^(-n+{funcion}) en ambos lados de la ecuación: ")

# Cambio de signo de los coeficientes para la representación final
output = f"{simbolo}^{funcion} "
for i in range(funcion):
    coeficiente = int(lista[i])
    # Cambio de signo
    coeficiente *= -1
    if coeficiente >= 0:
        if i > 0:
            output += f"+ {coeficiente}{simbolo}^{funcion-i-1} "
        else:
            output += f"{coeficiente}{simbolo}^{funcion-i-1} "
    else:
        output += f"- {abs(coeficiente)}{simbolo}^{funcion-i-1} "

# Al final, igualamos la suma de términos a 0
print(output)
output += "= 0"

print("Se ordena la función con cambio de signo: ")
print(output)
