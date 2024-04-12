import cmath

# Entrada del número de términos en la función de recurrencia
num_funciones = int(input("Ingrese el número de funciones que hay: "))
coeficientes = []

# Captura de coeficientes de cada término de la recurrencia
for i in range(1, num_funciones + 1):
    coeficiente = int(input(f"Ingrese el valor que multiplica f(n-{i}): "))
    coeficientes.append(coeficiente)

# Creación de la representación de la recurrencia
recurrencia = "f(n) = "
for i, coef in enumerate(coeficientes):
    if coef >= 0 and i > 0:
        recurrencia += f"+ {coef}f(n-{i+1}) "
    elif coef < 0:
        recurrencia += f"- {abs(coef)}f(n-{i+1}) "
    else:
        recurrencia += f"{coef}f(n-{i+1}) "

# Entrada del símbolo para la solución
while True:
    simbolo = input("Ingrese el símbolo de la ecuación (no puede ser 'c' o 'C'): ")
    if simbolo.lower() != 'c':
        break
    print("El símbolo 'C' o 'c' no es válido. Por favor, ingrese otro símbolo.")

# Solución de la ecuación característica
a = 1
b = -sum(coeficientes)  # Suma de coeficientes negada
c = coeficientes[-1] if len(coeficientes) > 1 else 0
discriminante = b**2 - 4*a*c

if discriminante >= 0:
    raiz1 = (-b - cmath.sqrt(discriminante)) / (2*a)
    raiz2 = (-b + cmath.sqrt(discriminante)) / (2*a)
    print("Las raíces son:", raiz1, raiz2)
else:
    print("No hay soluciones reales")

# Condiciones iniciales
condiciones = int(input("Ingrese el número de condiciones iniciales: "))
valores_condiciones = []
resultados_condiciones = []

for i in range(condiciones):
    valor = int(input(f"Ingrese el valor de f({i}): "))
    resultado = int(input(f"Ingrese el resultado de f({i}): "))
    valores_condiciones.append(valor)
    resultados_condiciones.append(resultado)

# Cálculo de C1 y C2 si las raíces son distintas
if raiz1 != raiz2:
    matriz = [[raiz1**n, raiz2**n] for n in valores_condiciones]
    vector = resultados_condiciones
    C1, C2 = np.linalg.solve(matriz, vector)
    print(f"Los valores de C1 y C2 son: {C1}, {C2}")
else:
    print("Manejo de raíces repetidas no implementado en este ejemplo.")

# Función general
print(f"La función general es: f(n) = {C1}({raiz1})^n + {C2}({raiz2})^n")
