numero_1: float = 0
numero_2: float = 0   
total: float = 0    

numero_1: float = float(input("informe o número: "))
numero_2: float = float(input("informe o número: "))
operador_matematico: str = input("Informe a operação desejada: +, -, *, /  ")

if operador_matematico == "+":
  total = numero_1 + numero_2
elif operador_matematico == "-":
    total = numero_1 - numero_2
elif operador_matematico == "*":
    total = numero_1 * numero_2
elif operador_matematico == "/":
    total = numero_1 / numero_2
    print("O resultado do calculo é: ", total)
else:
   print("Opção inválida.")

