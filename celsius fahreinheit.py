# Programa para transformação de medidas de temperatura

print("Bem vindo ao programa para transformar Celsius em Fahreinheit")

#Qual é a váriavel que determina qual IF do programa irá rodar

qual = input("Você tem o valor de Celsius, Fahreinheit ou Kelvin?")

#IF valor Celsius
if qual == 'c' :
    #Várivel c com input para se inserir o valor em celsius
    c = float(input("Insira o valor em Celsius para transformar:"))

    #var1 questiona para qual medida o usuário deseja transformar
    var1 = input("Você deseja transformar este valor para Kelvin ou Fahreinheit?")

    #Se for Fahreinheit entra neste IF:
    if var1 == 'f' :
        f = float((c * 9/5) + 32)
        print("Este é o valor em Fahreinheit:", f)
        exit()

    #Se for Kelvin entra neste IF:
    if var1 == 'k' :
        kelvin = float(c + 273)
        print("Este é o valor em Kelvin: ", kelvin)
        exit()

    #Else para valor inválido:
    else :
        print("Desculpe, este é um valor inválido.")

#If valor Fahrenheit
if qual == 'f' :

    #Váriavel F onde se insere o valor em Fahreinheit
    f = float(input("Insira o valor em Fahreinheit para transformar:"))

    #var2 questiona para qual medida deseja transformar
    var2 = input("Você deseja transformar este valor para Celsius ou Kelvin?")

    #IF para transformação para Celsius
    if var2 == 'c' :
        c = float((f - 32) / 1.8)
        print("Este é o valor em Celsius:", c)
        exit()

    #IF para transformação para Kelvin
    if var2 == 'k' :
        c = float((f - 32) / 1.8)
        k = float(c + 273)
        print("Este é o valor em Kelvin: ", k )
        exit()

    #Else para valor inválido
    else:
        print("Desculpe, este é um valor inválido.")

#If valor Kelvin
if qual == 'k':

    #Váriavel para inserir o valor em Kelvin
    k = float(input("Insira o valor em Kelvin que deseja transformar: "))

    #Var3 questiona Celsius ou Fahreinheit
    var3 = input("Você deseja transformar para Celsius ou Fahreinheit?" )

    #If transformação Kelvin para celsius
    if var3 == 'c':
        c = float(k - 273)
        print("Este é o valor em Celsius: ", c)
        exit()

    #If transformação Kelvin para Fahreinheit
    if var3 == "f":
        c = float(k - 273)
        f = float((c * 9/5) + 32)
        print("Este é o valor em Fahreinheit: ", f)
        exit()

    #Else valor incompatível
    else:
        print("Desculpe, este é um valor inválido.")

#Else valor incompátivel
else :
    print("Desculpe, valor inválido. Digite C ou F para descobrir celsius ou fahreinheit")
    exit()


