n = int(input("Tabla de multiplicar por el numero: "))

while n:
    if n > 0:
        for i in range(1, 11):
             print(f"La  multiplicación de {n} por {i} es {i*n}")
        break
    else:
         print("Valor invalido")