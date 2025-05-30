#dicionarios sao estruturas do tipo coleção que armazenam dados do tipo chave.add()

dict_carro: dict = {
  "marca" : "FIAT",
  "modelo" : "Chronos",
  "ano" : 2023,
  "cor" : "Preta"}

print("O modelo do carro é: ", dict_carro ["modelo"]) #buscando pela chave
print("O modelo do carro é: ", dict_carro.get ("ano")) #buscando pela chave

dict_proprietario: dict = {}
nome: str = input("Informe o nome: ")
cpf: str = input("Informe o cpf: ")
tel: str = input("Informe o telefone: ")

dict_proprietario["nome_prop"] = nome
dict_proprietario["cpf_prop"] = cpf
dict_proprietario["tel_prop"] = tel

# Retorna as chaves do dicionario
print(dict_carro.keys())

# print(dict_carro.values())

for item in dict_carro.keys():
  print(dict_carro.get(item))
