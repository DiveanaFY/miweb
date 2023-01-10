ph = int(input("introduzca el valor del pH (0-14) "))

if ph > 7:
    print("Básico")
elif ph < 7:
    print("ácido")
else:
    print("neutro")


