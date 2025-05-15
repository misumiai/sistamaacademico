print("codigo")

codigo_digitado = (input('''informe o codigo do produto: 
                                   100
                                   101
                                   102
                                   103
                                   104 
                                  - '''))
quantidade: int = int (input("informe a quantidade desejada: "))

match codigo_digitado:
   case "100":
      preco_final: float = 120 * quantidade
      print(f"o valor de {quantidade} camisa(s) é R$ {preco_final}")
   case "101":
      preco_final: float = 220 * quantidade
      print(f"o valor de {quantidade} saia(s) é R$ {preco_final}")
   case "102":
      preco_final: float = 180 * quantidade
      print(f"o valor de {quantidade} calça(s) é R$ {preco_final}")
   case "103":
      preco_final: float = 350 * quantidade
      print(f"o valor de {quantidade} vestido(s) é R$ {preco_final}")
   case "104":
      preco_final: float = 7.5 * quantidade
      print(f"o valor de {quantidade} meia(s) é R$ {preco_final}")
      
   case _:
      print("codigo invalido")

if preco_final >= 500:
 preco_final = preco_final - (preco_final * 0.10)
 print("valor com desconto: R$", preco_final)