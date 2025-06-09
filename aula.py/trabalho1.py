# Define uma função chamada ler_contatos.
def ler_contatos():
    # Início de um bloco "try", usado para capturar e tratar erros
    # Se acontecer um erro dentro do bloco "try" pula para o bloco "except"
    try:
        # Abre o arquivo "contatos.txt" no modo leitura ("r")
        # O "with" garante que o arquivo sera fechado automaticamente após o uso
        # A codificação "utf-8" permite ler caracteres especiais corretamente
        with open("contatos.txt", "r", encoding="utf-8") as arquivo:
            # imprime uma linha em branco e a mensagem "Contatos salvos:"
            print("\nContatos salvos:")
            # Percorre cada linha do arquivo
            for linha in arquivo:
                print(linha.strip())
    # Bloco "except" que sera executado se o erro FileNotFoundError acontecer
    except FileNotFoundError:
        # Exibe uma mensagem avisando que o arquivo não foi encontrado.
        # isso evita que o programa trave com uma mensagem de erro horrorosa para o usuario
        print("\nArquivo de contatos não encontrado.")

def inserir_contato():
    # solicita os dados do usuário
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o e-mail do contato: ")
    cidade = input("Digite a cidade do contato: ")

    # formata os dados como uma linha de texto
    contato = f"{nome} | {telefone} | {email} | {cidade}\n"

    # Abre (ou cria) o arquivo "contatos.txt" no modo "a" (de adicionar)
    # encoding="utf-8" garante que acentos e caracteres especiais sejam salvos corretamente
    with open("contatos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(contato)  # Escreve o contato no arquivo

    # confirma que o contato foi salvo
    print("Contato salvo com sucesso!")
