# Calculo de juros de uma poupança
# deposito inicial y la taxa de juros de una cuenta de ahorros
# Exhibir valores mes a mes para los 24 primeros meses
# Total de ganancias en los 24 meses.

cuenta = float(input("Deposito Inicial "))
taxa_juros = 2.17

mes = 1

while mes < 10:
    if mes % 2 == 0:
        nuevo_deposito = float(input("Cuanto quieres depositar este mes:  "))
        cuenta += nuevo_deposito
    juros = round((cuenta * taxa_juros) / 100, 2)
    print(f"Interes del mes {mes} = {juros}")
    cuenta += juros
    print(f"El valor de tu cuenta es de {round(cuenta, 2)}")
    mes += 1