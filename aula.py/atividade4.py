def quadrado():
    base = int(input("Informe a base: "))
    altura = int(input("Informe a altura: "))
    total = base * altura
    print("A área do quadrado é:", total)

def triangulo():
    base = int(input("Informe a base: "))
    altura = int(input("Informe a altura: "))
    total = (base * altura) / 2
    print("A área do triângulo é:", total)

def retangulo():
    base = int(input("Informe a base: "))
    altura = int(input("Informe a altura: "))
    total = base * altura
    print("A área do retângulo é:", total)

def circulo():
    raio = float(input("Informe o raio: "))
    pi = 3.14
    total = pi * (raio ** 2)
    print("A área do círculo é:", total)

def mostrar_menu():
    while True:
        print("\n--- MENU ---")
        print("1. Calcular área do quadrado")
        print("2. Calcular área do triângulo")
        print("3. Calcular área do retângulo")
        print("4. Calcular área do círculo")
        print("5. Sair")

        escolha = input("Escolha uma opção (1-5): ")

        if escolha == "1":
            quadrado()
        elif escolha == "2":
            triangulo()
        elif escolha == "3":
            retangulo()
        elif escolha == "4":
            circulo()
        elif escolha == "5":
            print("Você saiu do programa!")
            break
        else:
            print("Opção inválida, tente novamente.")

# Executa o menu
mostrar_menu()
