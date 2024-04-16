"""
Ignacio Rehbein
"""
import datetime

def fecha_de_nacimiento():
  while True:
    try:
      fecha1 = input("Ingrese su fecha de nacimiento 1 (dd/mm/yyyy): ")
      fecha1 = datetime.datetime.strptime(fecha1, "%d/%m/%Y")
      break
    except ValueError:
      print("Formato incorrecto, por favor intente de nuevo.")

  while True:
    try:
      fecha2 = input("Ingrese su fecha de nacimiento 2 (dd/mm/yyyy): ")
      fecha2 = datetime.datetime.strptime(fecha2, "%d/%m/%Y")
      break
    except ValueError:
      print("Formato incorrecto, por favor intente de nuevo.")

  if fecha1 == fecha2:
    print("Las fechas son iguales.")
  elif fecha1 < fecha2:
    print("La segunda persona es mayor.")
  elif fecha1 > fecha2:
    print("La primera persona es mayor.")

fecha_de_nacimiento()