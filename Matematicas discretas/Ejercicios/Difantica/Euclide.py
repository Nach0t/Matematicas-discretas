def euclides(a, b):
    valores = []
    numero2 = []
    print(f"Calculando el MCD de {a} y {b}")
    paso = 1
    while b != 0:
        q = a // b
        r = a % b
        print(f"{paso}. {a} = {q} * {b} + {r}")
        valores.append((a, b, q))
        numero2.append(a)
        a, b = b, r
        paso += 1
    print(f"Los valores usados son {numero2}, y el MCD es: {a}")
    return a, valores
