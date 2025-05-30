#Função é um bloco de codigo que pode ser chamado

def somar():
  num1: int = int(input("informe um numero: "))
  num2: int = int(input("informe um numero: "))

  total: int = num1 + num2
  print("A soma total é: ", total)

somar()
print("vamos somar novamente")
somar()
