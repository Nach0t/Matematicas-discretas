def euclides(a, b):
    valores_a = []
    print(f"Calculando el MCD de {a} y {b}")
    paso = 1
    while b != 0:
        q = a // b
        r = a % b
        print(f"{paso}. {a} = {q} * {b} + {r}")
        a, b = b, r
        valores_a.append(a)
        paso += 1
    print(f"Los valores usados son {valores_a}, y El MCD es: {a}")
    return a
