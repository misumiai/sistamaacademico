def quadrado():
  base: int = int(input("informe o base: "))
  altura: int = int(input("informe o altura: "))

  total: int = base * altura
  print("O total do quadrado é: ", total)

def triangulo():
  base: int = int(input("informe a base: "))
  altura: int = int(input("informe a altura: "))

  total: int = base * altura / 2
  print("O total do triangulo é: ", total)

def retangulo():
  base: int = int(input("informe o base: "))
  altura: int = int(input("informe o altura: "))

  total: int = base * altura
  print("O total do retangulo é: ", total)

def circulo():
  raio: float = float(input("informe o raio: "))
  pi: float = 3.14

  total: int = pi * (raio ** 2)
  print("O total do circulo é: ", total)

def mostrar_menu():
    print("\n--- MENU ---")
    print("1. calcular quadrado")
    print("2. calcular triângulo")
    print("3. calcular retângulo")
    print("4. calcular circulo")
    print("5. Sair")

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção (1-6): ")

    if escolha == "1":
  quadrado()

elif escolha == "2":
triangulo()

elif escolha == "3":
retangulo()

elif escolha == "4":
circulo()

elif escolha == "5":
print("você saiu do programa!")

else:
print("opção inválida")