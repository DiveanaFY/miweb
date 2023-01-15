salario = float(input("Digite aqui su salario: "))

if salario > 1250:
    total = salario * 0.10 + salario
    print(f"Tu nuevo salario es de: {total}")
else:
    otro = salario * 0.15 + salario
    print(f"Tu nuevo salario es de: {otro}")