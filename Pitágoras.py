print("Bem vindo a calculadora de pitágoras:")
print("Digite X no valor que deseja descobrir")
#Variáveis
a = input("Insira o valor da hipotenusa:")

b= input("Insira o valor do cateto 1:")

c = input("Insira o valor do cateto 2:")
#If Hipotenusa
if a == "x":
    b = float(b)
    c = float(c)
    print((b ** 2 + c ** 2) ** 0.5)
#If Cateto 1
if b == "x":
    a = float(a)
    c = float(c)
    print((a ** 2 - c ** 2) ** 0.5)
#If cateto 2
if c == "x":
    a = float(a)
    b = float(b)
    print((a ** 2 - b ** 2) ** 0.5)