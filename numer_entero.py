suma = 0
x = 0

while True:
    num = int(input("Escribe un numero entero:  "))
    suma += num
    if num == 0:
        break
    x += 1

print(f"La cantidad de numeros digitados fue de {x}")
print(f"La suma total de los numeros digitados fue de {suma}")
print(f"La media aritmetica de los numeros digitados es de {suma / x}")