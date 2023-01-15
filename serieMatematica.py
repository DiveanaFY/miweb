# resolver serie armonica  matematica

d = True

while d == True:
    num = int(input("Ingrese un numero entero positivo: "))
    if num > 0:
        d = False
        resultado = 0
        for i in range (1, num+1):
             resultado += (num/i)
        print(f"El resultado de la serie es {resultado}")

    else:
         print("Numero incorrecto")