# Escriba un programa para aprobar un prestamo bancario para la compra de una casa
# el programa debe preguntar el valor de la casa
# el salario y la cantidad de años a pagar
# el valor de la prestacion mensual no puede ser mayor a 30% del salario
# calcule el valor de prestacion como siendo el valor de la casa a comprar dividido por el numero de meses a pagar

valorCasa = float(input("Cual es el valor de la casa a comprar: "))
salario = float(input("Cual es tu salario: "))
anosPagar = int(input("Cantidad de años a pagar "))

salario_porcentual = salario * 0.30
prestacion_mensual = valorCasa / (anosPagar * 12)

if prestacion_mensual > salario_porcentual:
    print("Credito no aprobado")
elif prestacion_mensual <= salario_porcentual:
    print("Credito aprobado")

print(f"El 30% del salario mensual es de {salario_porcentual} \n y el valor de la prestacion mensual es de {prestacion_mensual}")
