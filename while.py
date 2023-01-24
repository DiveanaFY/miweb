# Necesitamos un conteo de 10 al 0 (10, 9 , 8 ... 0)  y al final un print "Se acabo el conteo"

x = int(input("Escribe un numero  "))
y = 1

while y <= x:
    if y % 2 != 0:
         print(y)
    y = y + 1