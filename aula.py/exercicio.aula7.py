print("Login")
senha: str = "adimin@2025"
senha: str = str(input("Digite a senha: "))

if senha == "adimin@2025":
   print("autenticação realizada com sucesso");
else:
   print("senha inválida")

conceito: str = str(input("Digite a nota do aluno: "))

if conceito == "A":
   print("Excelente");

elif conceito == "B":
   print("Otimo")
elif conceito == "C":
   print("Bom")
elif conceito == "D":
   print("Regular")
elif conceito == "E":
   print("Ruim")
elif conceito == "F":
   print("Nos vemos de novo no ano que vem...")

print("FORMA GEOMETRICA")
forma: str = str(input("Digite um numero geometrico: "))
  
if forma == "4":
  print("É um quadrado, eu acho")
elif forma == "15":
   print("É um retângulo, eu acho")  

   print("Dois NUMEROS")

numero_1: float = 0
numero_2: float = 0     

numero_1: float = float(input("informe o número 1: "))
numero_2: float = float(input("informe o número 2: "))

if numero_1 > numero_2:
   print("o maior numero é: ", numero_1);
else:
    numero_2 > numero_1
    print("o maior numero é: ", numero_2) 
    
    print("Maçãs")

macas = int(input("quantas maças? "))
preco = macas * 1.5
preco = preco - 5 
if preco > 20:
  print("valor a pagar: R$", round(preco,2))                 
elif preco < 20:
  print("valor a pagar: R$", preco) 

  print("media")
n1: float = float(input("informe a nota: "))
n2: float = float(input("informe a nota: "))
n3: float = float(input("informe a nota: "))
media = n1 + n2 + n3 / 3

print("A média das notas é: ", media)

print("Dólar")

valor_dolar: float = float (input("informe o valor recebido: U$"))
preco_real: float = 5.67
total: float = valor_dolar * preco_real
print("Você tem R$", total)

print("Negativo ou Positivo")
numero: float = float(input("Informe o numero: "))
if numero < 0:
   print("é um numero negativo")
elif numero > 0:
 print("é um numero positivo")

 print("lucro")

valor_produto: float = float (input("informe o valor do produto: R$ "))
valor_final: float = 0.0
lucro_a: float = 0.45
lucro_b: float = 0.30
 
 

if valor_produto < 20:
    percentual_real: float = (valor_produto * lucro_a)
    valor_final = valor_produto + percentual_real

else:
   percentual_real: float = (valor_produto * lucro_b)
   valor_final = valor_produto + percentual_real
   
print("O valor final do produto com o lucro ficou R$", valor_final)

vA: str = input("informe o valor: ")
vB: str = input("informe o segundo valor: ")
vB = vA 
print(vB)


dia_semana: int = int(input("informe o numero do dia: "))
match dia_semana:
   case 1: 
      print("domingo")
   case 2: 
      print("segunda-feira")
   case 3: 
      print("terça")
   case 4: 
      print("quarta")
   case 5: 
      print("quinta")
   case 6: 
      print("sexta")
   case 7:
      print("sabado")
   case _:
      print("valor invalido")


