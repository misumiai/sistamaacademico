# Define uma função chamada ler_contatos.
# Funções são blocos de código que só são executados quando chamados.
def ler_contatos():
    # Início de um bloco "try", usado para capturar e tratar erros.
    # Se acontecer um erro dentro do bloco "try", o Python pula para o bloco "except".
    try:
        # Abre o arquivo "contatos.txt" no modo leitura ("r").
        # O "with" garante que o arquivo será fechado automaticamente após o uso.
        # A codificação "utf-8" permite ler caracteres especiais corretamente (acentos, cedilha, etc).
        with open("contatos.txt", "r", encoding="utf-8") as arquivo:
            # Imprime uma linha em branco e a mensagem "Contatos salvos:"
            print("\nContatos salvos:")
            # Percorre cada linha do arquivo (ou seja, cada contato armazenado)
            for linha in arquivo:
                print(linha.strip())
    # Bloco "except" que será executado se o erro FileNotFoundError acontecer.
    # Esse erro ocorre quando o arquivo "contatos.txt" não existe no mesmo diretório do script.
    except FileNotFoundError:
        # Exibe uma mensagem avisando que o arquivo não foi encontrado.
        # Isso evita que o programa trave com uma mensagem de erro feia para o usuário.
        print("\nArquivo de contatos não encontrado.")

def inserir_contato():
    # Solicita os dados do usuário
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o e-mail do contato: ")
    cidade = input("Digite a cidade do contato: ")

    # Formata os dados como uma linha de texto
    # Cada campo é separado por um " | " para facilitar a leitura
    contato = f"{nome} | {telefone} | {email} | {cidade}\n"

    # Abre (ou cria) o arquivo "contatos.txt" no modo "a" (adicionar)
    # encoding="utf-8" garante que acentos e caracteres especiais sejam salvos corretamente
    with open("contatos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(contato)  # Escreve o contato no arquivo

    # Confirma que o contato foi salvo
    print("Contato salvo com sucesso!")
