nome = input("Insira seu nome: ")

idade = int(input("Insira sua idade:"))

salario = float(input("Insira seu salário: "))

sexo = input("Masculino ou feminino(Digite F ou M): ")

estcivil = input("Estado civil? (Solteiro, casado, viúvo ou divorciado)")

while len(nome) <= 3 :
    print("Por favor digite um nome maior")
    nome = input("Insira seu nome: ")

while idade > 150 or idade < 0 :
    print("Digite uma idade possível")
    idade = int(input("Insira sua idade:"))

while salario <= 0 :
    print("Salário inválido, digite um salário positivo: ")
    salario = float(input("Insira seu salário: "))

while (sexo != 'f') and (sexo != 'm') :
    print("Por favor digite M, para sexo masculino e F para sexo feminino:")
    sexo = input("Masculino ou feminino(Digite F ou M): ")

while (estcivil != 's') and (estcivil != 'c') and (estcivil != 'v') and (estcivil != 'd') :
    print("Por favor, indique seu estado civil pela letra inicial do mesmo: ")
    estcivil = input("Estado civil? (Solteiro, casado, viúvo ou divorciado)")

print("Parabéns, formulário completo!!!!!!!")
