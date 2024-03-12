import random
a,b,c,d = 0

def numero():
    ecuacion = a**4 + b **4 + c**4 
    resultado = d**4
    return ecuacion
    return resultado
    
ecu = numero(ecuacion)
res = numero(resultado)
while True:
    a,b,c,d = random.choice()
    if (ecu == res):
        print(f"los numeros que cumplen son: {a} {b} {c} {d}")  