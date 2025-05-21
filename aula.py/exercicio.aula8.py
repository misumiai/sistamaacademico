print("=============== LOGIN ===============")
usuario: str = (input("informe o nome do usuario: "))
senha: str = (input("informe a senha do usuario: "))

if usuario == "proz@25" and senha == "admin123":
    print("Logado com sucesso.")
else: 
    print("Usuario ou senha invalidos.")