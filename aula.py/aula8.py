'''
Para aposentar é necessario ter 65 anos de idade ou 35 anos de contribuição. O sistema deve fazer a verificação e dizer se o usuario tem direito ou nao.

'''

print("=============== INSS ===============")
idade: int = int(input("informe a idade do contribuinte: "))
tempo_contribuição: int = int(input("informe o tempo de contribuição: "))

if idade >= 65 or tempo_contribuição >= 35:
    print("pode se aposentar.")
else: 
    print("Aposentadoria negada! Nao seja preguiçoso.")


