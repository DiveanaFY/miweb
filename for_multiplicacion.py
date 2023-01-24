
# while numero <= 10:
#     print(f"{tabla} x {numero} = {tabla * numero}")
#     numero += 1
#     if numero == 11:
#         numero = 1
#         tabla += 1
#         if tabla == 11:
#             break

# while tabla <= 9:
#     numero = 1
#     tabla += 1
#     while numero <= 10:
#         print(f"{tabla} x {numero} = {tabla * numero}")
#         numero += 1

for tabla in range(1, 11):
    print(f"Vamos a hacer la tabla del {tabla}")
    for numero in range(1, 11):
        print(f"{tabla} x {numero} = {tabla * numero}")