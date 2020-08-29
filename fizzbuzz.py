a = int(input("Insira um valor: "))
b = a % 3
c = a % 5
if b == 0 and c == 0:
    print("Fizzbuzz")
else:
    print(a)