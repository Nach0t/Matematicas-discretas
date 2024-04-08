# fubcion que calcula el MCD de dos numeros
def euclides(a, b):
    valores_a = []
    # Imprimir el mensaje inicial
    print(f"Calculando el MCD de {a} y {b}")
    paso = 1  # Iniciar un contador para los pasos
    # Iterar hasta que b sea 0
    while b != 0:
        q = a // b
        r = a % b
        print(f"{paso}. {a} = {q} * {b} + {r}")  # Mostrar el proceso con el número de paso
        a, b = b, r
        valores_a.append(a)
        paso += 1  # Incrementar el contador de pasos para la siguiente iteración
    print(f"Los valores usados son {valores_a}, y El MCD es: {a}")
    return a

# Solicitar al usuario que ingrese dos números
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

# Llamar a la función euclides e imprimir el MCD
euclides(a, b)