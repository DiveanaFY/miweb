dia_alquilado = 60
cada_km = 0.15

kilometros = int(input("Cantidad de kilometros recorridos: "))
dias = int(input("Cantida de dias alquilado: "))

def calculo(a,b):
    return a * b 

precio_km = calculo(kilometros, cada_km)
precio_dias = calculo(dias, dia_alquilado)

total = precio_km + precio_dias

print(f"total precio kilometros {precio_km}")
print(f"total precio dias {precio_dias}")
print(f"Total a pagar {total}")
