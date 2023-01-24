L = []
A = []
x = 0

while x < 2:
    n = int(input("Digite un numero entero positivo:  "))
    b = int(input("Digite un numero entero positivo:  "))
    L.append(n)
    A.append(b)
    Z = L[:]
    Z.extend(A)
    x += 1

x = 0
while x < len(Z):
    print(f"{x} = {Z[x]}")
    x += 1