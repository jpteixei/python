#fatorial
a = int(input("Insira um valor: "))
contador = 1
resultado = 1
while contador <= a :
    resultado = contador * resultado
    contador = contador + 1
print(resultado)