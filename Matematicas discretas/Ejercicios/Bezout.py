def bezout(valores_a):
    x, y = 1, 0  # Inicialmente para el último valor de a (que es el MCD)
    total_pasos = len(valores_a) - 1
    # Iteramos desde el penúltimo valor de a hasta el primer valor de a
    for i in range(total_pasos - 1, -1, -1):
        q = valores_a[i] // valores_a[i + 1]
        # Actualizamos x e y
        x, y = y, x - y * q
        # Ajuste del índice de paso para mostrar correctamente, comenzando desde 1
        paso_actual = total_pasos - i
        print(f"Paso {paso_actual}: r = {valores_a[i + 1]} = {valores_a[i]} - {q} * {valores_a[i + 1]}")
    return x, y
