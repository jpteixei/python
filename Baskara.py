print("Bem vindo a calculadora de Bhaskara")

a = float(input("Digite o valor de A:"))

b = float(input("Digite o valor de B:"))

c = float(input("Digite o valor de C:"))

descri = float(((b ** 2) - (4 * a * c)))

if descri == 0:
    resultum = float((-b / (2 * a)))
    print("Sua equação só tem um resultado:", resultum)
    exit()

if descri < 0:
    print("Desculpe não podemos extrair raízes negativas")
    exit()

if descri > 0:
    resultmais = float((-b+(descri ** 0.5))/(2 * a))
    resultmenos = float((-b-(descri ** 0.5))/(2 * a))
    print("Os resultados da sua expressão são:", resultmais,"e", resultmenos)



