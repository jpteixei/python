#validação notas
ncorreta = 9
ndigitada = 0
ndigitada = int(input("Digite uma nota: "))
if ncorreta == ndigitada :
    print("Parabéns você acertou de primeira!!!")
else:
    while ncorreta != ndigitada :
        print("Ops, nota incorreta")
        ndigitada = int(input("Digite uma nota: "))
    print("Parabéns você digitou a nota correta")