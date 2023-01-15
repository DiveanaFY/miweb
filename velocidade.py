velocidad = int(input("Cual es la velocidad del carro:  "))
multa = 0

if velocidad <= 80:
    print("Velocidad adecuada")
elif velocidad > 80:
    print("Has sido multado") 
    for i in range(80, velocidad):
        multa += 5
    print(f"La multa es: {multa}")   

