import random

valor_1 = random.randint(1, 20)
valor_2 = random.randint(1, 20)

print(f"calcular la multiplicacion de {valor_1} x {valor_2}")

respuesta = 0
contador = 1

while contador <= valor_2:
     respuesta = respuesta + valor_1
     contador = contador + 1

print (f"{valor_1} x {valor_2} = {respuesta}")