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
output = f"{simbolo}^{funcion} +"
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

if funcion == 2:
    a = 1
    b = int(lista[0])
    c = int(lista[1])

    discriminante = (b**2 - 4*a*c)
    if discriminante >= 0:
        valor1 = (-b - (discriminante ** 0.5)) / (2*a)
        valor2 = (-b + (discriminante ** 0.5)) / (2*a)

        print("Los valores son:", valor1, valor2)
    else:
        print("No hay soluciones reales")



output = f"{simbolo}(n) = C1({valor1})^n + C2({valor2})^n"
print(output)


# Entrada del número de condiciones iniciales y almacenamiento de las mismas
condiciones = int(input("Ingrese el número de condiciones iniciales: "))

condicion = []
resultado = []

for i in range(condiciones):
    cond = int(input(f"Ingrese el valor de f({i}): "))
    resultados = int(input(f"Ingrese el resultado de f({i}): "))
    condicion.append(cond)
    resultado.append(resultados)

# Asegúrate de que valor1 y valor2 sean flotantes o enteros, según sea necesario
valor1 = float(valor1) if isinstance(valor1, str) else valor1
valor2 = float(valor2) if isinstance(valor2, str) else valor2

# Verifica que se hayan ingresado al menos dos condiciones para calcular C1 y C2
if len(resultado) >= 2:
    f0 = resultado[0]
    f1 = resultado[1]

    # Calcula C1 y C2 usando el sistema de ecuaciones lineales derivado de las condiciones iniciales
    if valor1 != valor2:
        denominador = valor1 - valor2
        c1 = (f1 - valor2 * f0) / denominador
        c2 = (valor1 * f0 - f1) / denominador

        print(f"Los valores de C1 y C2 son: {c1}, {c2}")
        output = f"{simbolo}(n) = {c1} * ({valor1})^n + {c2} * ({valor2})^n"
        print(f"La solución es: {output}")
    else:
        print("Si me dan ganas los agregos lmao.")
else:
    print("Se requieren al menos dos condiciones iniciales para calcular C1 y C2.")