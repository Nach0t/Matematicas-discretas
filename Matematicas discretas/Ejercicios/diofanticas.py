def difantia(a, b):
    valores_a = []
    valores_b = []
    # Imprimir el mensaje inicial
    print(f"Calculando la ecuación diofántica de {a} y {b}")
    paso = 1  # Iniciar un contador para los pasos
    # Iterar hasta que b sea 0
    while b != 0:
        q = a // b
        r = a % b
        print(f"{paso}. {a} = {q} * {b} + {r}")  # Mostrar el proceso con el número de paso
        a, b = b, r
        valores_a.append(a)
        valores_b.append(b)
        paso += 1  # Incrementar el contador de pasos para la siguiente iteración
    print(f"Los valores usados son {valores_a}, y El MCD es: {a}")
    return a

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
difantia(a, b)