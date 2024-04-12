import Euclide 

def bezout(valores_a):
    x, y = 1, 0  # Inicialmente para el último valor de a (que es el MCD)
    for i in range(len(valores_a) - 2, -1, -1):
        x, y = y, x - y * (valores_a[i] // valores_a[i + 1])
    return x, y

