nusuario = input("Insira um nome de usuário: ")
senha = input("Insira uma senha: ")
while senha == nusuario:
    print("Sua senha é igual ao seu nome de usuário")
    print("Por favor digite outra senha")
    nusuario = input("Insira um nome de usuário: ")
    senha = input("Insira uma senha: ")
print("Senha e nome de usuário registrados")