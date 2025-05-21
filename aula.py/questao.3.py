contador: int = 0
num1: int = 0
maior: int = 0
while contador < 3:

    num1: int = int(input("digite o numero: "))
    if num1 > maior:
        maior = num1
        contador = contador + 1

print("o maior numero é: ", maior)