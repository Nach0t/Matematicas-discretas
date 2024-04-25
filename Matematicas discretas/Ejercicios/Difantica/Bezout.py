import Euclide
def bezout(valores):
    if not valores:
        return 0, 0

    x, y = 0, 1
    total_pasos = len(valores)
    for i in range(total_pasos - 2, -1, -1):
        a, b, q = valores[i]
        x, y = y, x - q * y
        paso_actual = total_pasos - i
        print(f"Paso {paso_actual}: r = {valores[i + 1][1]} = {a} - {q} * {b}")
    return x, y
