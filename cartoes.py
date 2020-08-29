mcartao = int(input("Digite o número do seu cartão de crédito"))

pilhacartoes = int(input("Quantos cartões tem na lista? "))

lcartao = 0

while mcartao != lcartao :
    lcartao = int(input("Digite o número do próximo cartão"))
    if lcartao == mcartao :
        print("Parabéns você achou seu cartão de crédito.")
        exit()
    else:
        print("Ops, este não é o seu cartão")