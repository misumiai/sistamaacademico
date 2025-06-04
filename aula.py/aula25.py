def convert_euro(valor_real: float):
    valor_euro: float = valor_real / 6.42
    print(f"O valor em euro é €{valor_euro:.2f}")

def convert_dolar(valor_real: float):
    valor_dolar: float = valor_real / 5.64
    print(f"O valor em dólar é ${valor_dolar:.2f}")

def convert_libra(valor_real: float):
    valor_libra: float = valor_real / 7.63
    print(f"O valor em libras é £{valor_libra:.2f}")

# Essas linhas devem estar fora das funções
valor_real: float = float(input("Informe o valor em reais (R$): "))
convert_euro(valor_real)
convert_dolar(valor_real)
convert_libra(valor_real)
