def euclides(a, b):
    valores_a = []  # Lista para almacenar todos los valores de 'a' usados
    while b != 0:
        valores_a.append(a)  # Añadir el valor actual de 'a' a la lista
        a, b = b, a % b
    valores_a.append(a)  # Añadir el último valor de 'a', que es el MCD
    print("Todos los valores de 'a' usados:", valores_a)
    print("El máximo valor de 'a' usado:", max(valores_a))
    return a  # Retornar el MCD

# Solicitar al usuario que ingrese dos números
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

# Llamar a la función euclides e imprimir el MCD
mcd = euclides(a, b)
print("El MCD de", a, "y", b, "es:", mcd)
