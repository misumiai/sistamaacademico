numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

nume = int(input("Digite um número: "))
while nume >= 0:
    print(nume)
    nume -= 1

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a >= b and a >= c:
    print("O maior número é:", a)
elif b >= a and b >= c:
    print("O maior número é:", b)
else:
    print("O maior número é:", c)

soma = 0
num = int(input("Digite um número positivo (ou negativo para parar): "))

while num >= 0:
    soma += num
    num = int(input("Digite outro número positivo (ou negativo para parar): "))

print("Soma dos números positivos:", soma)

senha_correta = "1234"
senha = input("Digite a senha: ")

while senha != senha_correta:
    print("Senha incorreta. Tente novamente.")
    senha = input("Digite a senha: ")

print("Acesso concedido.")

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode tirar a carteira de motorista.")
else:
    print("Você ainda não pode tirar a carteira de motorista.")


numer = int(input("Digite um número para ver a tabuada: "))
contador = 1

while contador <= 10:
    print(f"{numer} x {contador} = {numer * contador}")
    contador += 1


number = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
contador = 1

while contador <= number:
    fatorial *= contador
    contador += 1

print("Fatorial:", fatorial)

