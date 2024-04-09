import Euclide 

def difanticas(a, b):
    resultado = Euclide.euclides(a, b)  # Usa directamente a y b que se pasan como argumentos

    if resultado == 1:
        print("La ecuación tiene solución.")
    else:
        print("La ecuación no tiene solución.")

# Este es el único lugar donde se solicitan los números a y b
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

# Luego, llama a la función 'difanticas' pasando los números a y b
difanticas(a, b)
