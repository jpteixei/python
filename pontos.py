x1 = int(input("Insira o valor do X1: "))
y1 = int(input("Insira o valor do Y1: "))
x2 = int(input("Insira o valor do X2: "))
y2 = int(input("Insira o valor do Y2: "))

pit = float(((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5))

if pit >= 10 :
    print("Longe")
else:
    print("Perto")