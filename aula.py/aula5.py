num1: int = 28
num2 = 17
resultado: bool = False #bool so usada em True ou False

print(num1 > num2) # maior
print(num1 < num2) # menor
print(num1 >= num2) # maior ou igual
print(num1 <= num2) # menor ou igual
print(num1 != num2) # diferente
print(num1 == num2) # igualdade

ano: int = int(input("Digite seu ano de nascimento: "))

if ano <= 2025:
   print("Bem vindo!!!!!!!!!!!!!!!!!!");
else:
   print("Não foi aceito")