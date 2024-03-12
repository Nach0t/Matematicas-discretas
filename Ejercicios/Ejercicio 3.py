def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def n_primos(n):
    numeros_primos = []
    numero = 2
    while len(numeros_primos) < n:
        if es_primo(numero):
            numeros_primos.append(numero)
        numero += 1
    return numeros_primos

cantidad = int(input("Ingrese la cantidad de números primos que desea mostrar: "))
primos = n_primos(cantidad)
print(f"Los primeros {cantidad} números primos son: {primos}")
