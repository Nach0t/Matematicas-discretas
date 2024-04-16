"""
Ignacio Rehbein
"""
def ecuacion_2Grado(a, b, c):
    # Calculamos el discriminante
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + discriminante**0.5) / (2*a)
        x2 = (-b - discriminante**0.5) / (2*a)
        print(f"Las soluciones son: x1={x1}, x2={x2}")
    elif discriminante == 0:
        x = -b / (2*a)
        print(f"La solución es: x={x}")
    else:
        print("La ecuación no tiene solución real.")

# Solicitamos los valores de a, b y c
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
ecuacion_2Grado(a, b, c)