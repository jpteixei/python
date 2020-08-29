num = int(input("Insira um número que para saber se é par ou impar: "))
ver = num % 2
if ver == 0 :
    print("O número", num, "é par")
else:
    print("O número", num, "é impar")