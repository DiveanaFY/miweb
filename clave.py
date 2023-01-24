tabla = 1
numero = 1

while tabla <= 10:
    print(f"{tabla} x {numero} = {tabla * numero}")
    numero += 1
    if numero == 11:
        numero = 1
        tabla += 1