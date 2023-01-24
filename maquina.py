total = 0

while True:
    costo = 0
    codigo = int(input("Digite el codigo del producto:  "))
    if codigo == 0:
        break
    cantidad = float(input("Digite la cantidad comprada:  "))
    if codigo == 1:
        print("precio de 0.50")  
        costo += (0.50 * cantidad)
    elif codigo == 2:
        print("precio de 1.'00")
        costo += (1.00 * cantidad)
    elif codigo == 3:
        print("precio de 4,00") 
        costo += (4.00 * cantidad)
    elif codigo == 5:
        print("precio de 7,00")
        costo += (7.00 * cantidad) 
    elif codigo == 9:
        print("precio de 8.00")
        costo += (8.00 * cantidad)
    else:
        print("codigo errado") 
    total += costo

    print(f"costo por producto {costo}")

print(f"El valor total de tus compras es de {total}")