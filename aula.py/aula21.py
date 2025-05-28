cidades: list = ["betim", "contagem", "RN", "juatuba", "ibirite"]
print(cidades)

# Percorrendo uma lista
for cidade in cidades:
    print("você está em:", cidade)

# Exibe o tamanho da lista
tamanho_lista: int = len(cidades)
print("o tamanho do array:", tamanho_lista)

# Percorrendo com índice
for i in range(len(cidades)):
    print("tradicional:", cidades[i])

# Verificando se "sarzedo" está na lista
if "sarzedo" in cidades:
    print("cidade encontrada")

    for i in range(len(cidades)):
        if cidades[i] == "sarzedo":
            print("índice:", i)
            break

# Buscar índice
print("índice de 'contagem':", cidades.index("contagem"))

# Verificar se um item está na lista
print("ouro preto está na lista?", "ouro preto" in cidades)

# Remoção de elementos
cidades.pop(2)  # remove "RN"
print(cidades)

cidades.remove("betim")
print(cidades)

# Ordenar lista em ordem reversa
cidades.sort(reverse=True)
print(cidades)


