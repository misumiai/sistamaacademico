#lista de compras

lista_compras:list = []

while True:

    opcao: str = input('''=============sistema de compras==============
                                       A: inserir elemento da lista 
                                       B: ver elmentos da lista
                                       c: remover elemento da lista
                                       X: encerrar o progama ''')
    

    match opcao:
       case "A": #inserir lista
        item_inserir: str = input("inserir - digite o produto: ")
        #adicionar elmento final 
        lista_compras.append(item_inserir)
        print("\n")
       
       case "B" :# ver a lista 
        print("============= itens da lista ==============")
        for item_da_lista in lista_compras:
          print(item_da_lista)
       
       case "C":  #encerrar o loop
        item_excluido: str = input("informe o elemento a ser excluido:")
        lista_compras.remove(item_excluido)
        print("\n")
        
       case "X": #excluir lista
          print('''''''''''''progama encerrdo''''''''''''')
          break
      
       
        
          