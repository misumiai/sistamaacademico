frutas = ["maçã", "banana", "laranja", "uva", "melancia", "pera", "kiwi", "abacaxi", "morango", "coco"]

fruta_usuario = input("Digite o nome de uma fruta: ")

if fruta_usuario.lower() in frutas:
    print("A fruta está na lista.")
else:
    print("A fruta não está na lista.")

nomes = ["Ana", "Carlos", "Bruna", "Diego", "Eduarda", "Felipe", "Giovana", "Henrique", "Isabela", "João"]

# Ordem alfabética
nomes_ordenados = sorted(nomes)
print("Nomes em ordem alfabética:")
print(nomes_ordenados)

# Ordem inversa
nomes_inverso = list(reversed(nomes))
print("Nomes na ordem inversa em que foram declarados:")
print(nomes_inverso)

planetas = ["Mercúrio", "Vênus", "Terra", "Marte", "Júpiter", "Saturno", "Urano", "Netuno"]

posicao = int(input("Digite a posição do planeta (de 1 a 8): "))

if 1 <= posicao <= 8:
    print("O planeta na posição", posicao, "é:", planetas[posicao - 1])
else:
    print("Posição inválida.")


notas = []

for i in range(5):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print("A média das notas é:", media)


