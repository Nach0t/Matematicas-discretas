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

print(output)

# Entrada del símbolo para la solución de EDO
simbolo = input("Ingrese el símbolo de la ecuación: ")

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

# Notificación de multiplicación por un factor adicional según la recurrencia
print(f"Se multiplica por: {simbolo}^(-n+{funcion})")

output = f"{simbolo}^{funcion} = "
for i in range(funcion):
    coeficiente = int(lista[i])
    # Calculamos el exponente para el término actual, que decrece desde el valor máximo 'funcion - 1'
    exponente_actual = funcion - i - 1
    if coeficiente >= 0:
        if i > 0:  # Añade un '+' solo si no es el primer término
            output += f"+ {coeficiente}{simbolo}^{exponente_actual} "
        else:
            output += f"{coeficiente}{simbolo}^{exponente_actual} "
    else:
        output += f"- {abs(coeficiente)}{simbolo}^{exponente_actual} "

print(output)
output = f"{simbolo}^{funcion} "
for i in range(funcion):
    coeficiente = int(lista[i])
    exponente_actual = funcion - i - 1
    if coeficiente >= 0:
        if i > 0:  # Añade un '+' solo si no es el primer término
            output += f"+ {coeficiente}{simbolo}^{exponente_actual} "
        else:
            output += f"{coeficiente}{simbolo}^{exponente_actual} "
    else:
        output += f"- {abs(coeficiente)}{simbolo}^{exponente_actual} "

# Al final, igualamos la suma de términos a 0
output += "= 0"

print("Se ordena la funcion: ")
print(output)
