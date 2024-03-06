def numero_primo(primo):
    numeros = 0
    list = []
    for i in range(1, 10):
        if primo % i == 0:
            numeros += 1
            list.append(i)
        
    if numeros >= 2:
        print(f"No es primo, es divisible en: {list}")
    else:
        print("Es primo")
                
primo = int(input("Ingrese un numero: "))
print(numero_primo(primo))