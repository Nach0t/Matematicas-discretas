import Euclide
import Bezout

def difanticas(a, b):
    # Capturamos tanto el MCD como los valores_a que se usan para Bézout
    mcd, valores_a = Euclide.euclides(a, b)  
    
    if mcd == 1:
        print("La ecuación tiene solución.")
    else:
        print("La ecuación no tiene solución.")

    # Pedimos al usuario si desea aplicar Bézout y corregimos la llamada con capitalize
    accion = input("¿Quieres aplicar Bezout?: (Si/No) ").capitalize()

    if accion == "Si":
        # Ahora pasamos correctamente valores_a a la función bezout
        x, y = Bezout.bezout(valores_a)
        print(f"Los coeficientes de Bézout son: x={x}, y={y}")

# Este es el único lugar donde se solicitan los números a y b
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

# Luego, llama a la función 'difanticas' pasando los números a y b
difanticas(a, b)
