def frigonachi(n):
    fibonacci_seq = [0, 1] 
    for i in range(2, n):
        next_num = fibonacci_seq[-1] + fibonacci_seq[-2]  
        fibonacci_seq.append(next_num)
    return fibonacci_seq

def frigonachi2(limite):
    fibonacci_seq = [0, 1]
    n = 2  # Iniciamos desde el tercer término
    while fibonacci_seq[-1] + fibonacci_seq[-2] <= limite:
        siguiente_numero = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(siguiente_numero)
        n += 1
    if len(fibonacci_seq) == 2:
        return "El límite es menor que los dos primeros términos de Fibonacci."
    else:
        return n - 1, n

opcion = input("¿Qué versión de Fibonacci quieres generar? (1 o 2): ")

if opcion == '1':
    n = int(input("Ingrese cuántos números de Fibonacci quieres ver: "))
    fib_sequence = frigonachi(n)
    print("Secuencia de Fibonacci:", fib_sequence)
elif opcion == '2':
    limite = int(input("Ingrese el límite para la secuencia de Fibonacci: "))
    num = frigonachi2(limite)
    if isinstance(num, tuple):
        print("El número que supera el límite podría estar entre los términos", num[0] + 1, "y", num[1] + 1)
    else:
        print(num)
else:
    print("Opción no válida. Por favor, elija 1 o 2.")