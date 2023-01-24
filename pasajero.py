# Escribe un programa que pregunte la distancia que una persona desea recorrer en kilometros, calcule el precio del pasaje
# Cobrando 0,50 x km, para viajes de hasta 200 km y 0,45 para viajes mas largos

distancia = int(input("Que distancia deseas recorrer en kilometros: "))
pasaje = 0

if distancia < 200:
    for km in range(distancia):
        pasaje += 0.50
    print (f"El valor del pasaje es {pasaje}")
else:
    for km in range(distancia):
        pasaje += 0.45
    print(f"El valor de tu pasaje es {pasaje}")