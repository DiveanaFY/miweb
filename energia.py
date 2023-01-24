# Calcule el precio a pagar por la energia electrica
# pregunte la cantida de Kwh consumida y el tipo de instalacion 
# R = residencias I = Industrias C = Comercios 

kwh = float(input("Digite la cantidad de KwH consumida:  "))
instalacion = input("Digite el tipo de instalacion:   ").upper()
costo = 0

if instalacion == "R":
    if kwh <= 500:
         print("su taxa a pagar es de 0.40")
         costo += kwh * 0.40
    else:
         print("su taxa a pagar es de 0.65")
         costo += kwh * 0.65

if instalacion == "I":
    if kwh <= 5000:
        print("Su taxa a pagar es de 0.55")
        costo += kwh * 0.55
    else:
        print("Su taxa a pagar es de 0.60")
        costo += kwh * 0.60
        
if instalacion == "C":
    if kwh <= 1000:
        print("Su taxa a pagar es de 0.55")
        costo += kwh * 0.55
    else: 
        print("Su taxa a pagar es de 0.60")

print(f"El costo electrico total es de {round(costo, 2)}")
# valor total es kwh * consumo