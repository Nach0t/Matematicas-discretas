def modular(a, b):
    if b <= 0:
        print("El valor de b debe ser positivo pero quedaria:.")
        q = a // b  # Calcula el cociente
        r = a % b   # Calcula el residuo
        print(f"{a} ≡ {r} (mod {b})")
        return a, b, q, r
    elif b >= 0:
      print("Queda: ")
      q = a // b  # Calcula el cociente
      r = a % b   # Calcula el residuo
      print(f"{a} ≡ {r} (mod {b})")
      return a, b, q, r

# Lectura de entradas
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

# Llamada a la función con las entradas proporcionadas
modular(a, b)
