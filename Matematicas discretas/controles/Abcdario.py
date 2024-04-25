a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
k = 11
l = 12
m = 13
n = 14
ñ = 15
o = 16
p = 17
q = 18
r = 19
s = 20
t = 21
u = 22
v = 23
w = 24
x = 25
y = 26
z = 27

def crypto():
  print("Ingresa el mensaje a cifrar")
  mensaje = input()
  mensaje = mensaje.lower()
  mensaje = mensaje.replace(" ", "")
  mensaje = mensaje.replace("á", "a")
  mensaje = mensaje.replace("é", "e")
  mensaje = mensaje.replace("í", "i")
  mensaje = mensaje.replace("ó", "o")
  mensaje = mensaje.replace("ú", "u")
  mensaje = mensaje.replace("ü", "u")
  mensaje = mensaje.replace("ñ", "n")
  mensaje = mensaje.replace(",", "")
  mensaje = mensaje.replace(".", "")
  mensaje = mensaje.replace(";", "")
  mensaje = mensaje.replace(":", "")
  mensaje = mensaje.replace("!", "")
  mensaje = mensaje.replace("?", "")
  mensaje = mensaje.replace("(", "")
  mensaje = mensaje.replace(")", "")
  mensaje = mensaje.replace("¡", "")
  mensaje = mensaje.replace("¿", "")
  mensaje = mensaje.replace("0", "")
  mensaje = mensaje.replace("1", "")
  mensaje = mensaje.replace("2", "")
  mensaje = mensaje.replace("3", "")
  mensaje = mensaje.replace("4", "")
  mensaje = mensaje.replace("5", "")
  mensaje = mensaje.replace("6", "")
  mensaje = mensaje.replace("7", "")
  mensaje = mensaje.replace("8", "")
  mensaje = mensaje.replace("9", "")

  cifrado = ""
  for char in mensaje:
    if char.isalpha():
      cifrado += str(globals()[char]) + " "
  print("Mensaje cifrado:", cifrado.strip())

crypto()