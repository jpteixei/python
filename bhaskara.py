print("Bem vindo a calculadora de Bhaskara")

a = float(input("Digite o valor de A:"))

b = float(input("Digite o valor de B:"))

c = float(input("Digite o valor de C:"))

descri = float(((b ** 2) - (4 * a * c)))

if descri == 0:
    resultum = float((-b / (2 * a)))
    print("A raiz deste equação é ", resultum)
    exit()

if descri < 0:
    print("Esta equação não possui raízes reais")
    exit()

if descri > 0:
    resultmais = float((-b+(descri ** 0.5))/(2 * a))
    resultmenos = float((-b-(descri ** 0.5))/(2 * a))
    if resultmais > resultmenos :
        print("As raízes desta equação são", resultmenos,"e", resultmais)
    if resultmenos > resultmais :
        print("As raízes desta equação são", resultmais, "e", resultmenos)