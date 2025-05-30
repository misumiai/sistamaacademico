#Função é um bloco de codigo que pode ser chamado

def somar():
  num1: int = int(input("informe um numero: "))
  num2: int = int(input("informe um numero: "))

  total: int = num1 + num2
  print("A soma total é: ", total)

def subtrair():
  num1: int = int(input("informe um numero: "))
  num2: int = int(input("informe um numero: "))

  total: int = num1 - num2
  print("A soma total é: ", total)

somar() #invocando a função
print("vamos somar novamente")
somar() #invocando função
subtrair() #invocando função

