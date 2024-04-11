funcion = int(input("Ingrese el numero de funcion que hay: "))

lista = []

for i in range(1, funcion + 1):
  a = input(f"Ingrese el valor que multiplica  f(n-{i}): ")
  lista.append(a)
  
output = "f(n) = "
for i in range(funcion):
    coeficiente = int(lista[i])
    if coeficiente >= 0:
        if i > 0:  # Añade un '+' solo si no es el primer término
            output += f"+ {coeficiente}f(n-{i+1}) "
        else:
            output += f"{coeficiente}f(n-{i+1}) "
    else:
        # Aquí aplicamos el cambio solicitado
        output += f"- {abs(coeficiente)}f(n-{i+1}) "

print(output)