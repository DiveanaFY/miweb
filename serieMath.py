comprobar = True

while comprobar == True:
    n = int(input("Ingresa un numero entero positivo "))
    if n > 0:
         resultado = 1
         for i in range(2,n+1):
             if i % 2 == 0:
                 resultado = resultado / (1/i)
             else:
                 resultado = resultado * (1/i)
         print(f"El resultado es {resultado}")
         comprobar = False
    else:
         print("Valor invalido")
