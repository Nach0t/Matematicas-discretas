def frigonachi(n):
    fibonacci_seq = [0, 1]  #
    for i in range(2, n):
        next_num = fibonacci_seq[-1] + fibonacci_seq[-2]  
        fibonacci_seq.append(next_num)
    return fibonacci_seq

n = input("Ingrese los numeros que quieras ver: ")
fib_sequence = frigonachi(n)
print("Fibonacci sequence:", fib_sequence)
