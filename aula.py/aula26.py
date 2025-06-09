VALOR_HORA_BASE: float = 45.90
def calcula_salario_bruto(numeroHoras: float):
    salario_bruto: float = numeroHoras * VALOR_HORA_BASE
    print("O salário Bruto é R$", salario_bruto)
    return salario_bruto
 
def calcula_inss(salario_bruto: float):
    percentual: float = 0.0
    if salario_bruto <= 1518:
        percentual = 0.075
    elif salario_bruto > 1518 and salario_bruto < 2793.88:
        percentual = 0.09
    elif salario_bruto > 2793.88 and salario_bruto < 4190.83:
        percentual = 0.12
    else:
        percentual = 0.14
    valor_inss: float = salario_bruto * percentual
    print("O valor do INSS é", valor_inss)

def calcula_fgts(salario_bruto: float):
    fgts: float = salario_bruto * 0.08
    print("O FGTS é R$", fgts)

def calcula_imposto_renda(salario_bruto: float):
    aliquota: float = 0.0
    if salario_bruto > 2428.80 and salario_bruto < 2826.65:
        aliquota = 0.075
    elif salario_bruto > 2826.65 and salario_bruto < 3751.05:
        aliquota = 0.15
    elif salario_bruto > 3751.05 and salario_bruto < 4664.68:
        aliquota = 0.225
    elif  salario_bruto > 4664.68:
        aliquota = 0.275

    imposto_renda: float = salario_bruto * aliquota
    print("O imposto de renda a ser pago é: R$", imposto_renda)

quantidade_horas: float = float(input("Informe a quantidade de horas trabalhadas: "))
valor_salario:float = calcula_salario_bruto(quantidade_horas)
calcula_inss(valor_salario)
calcula_fgts(valor_salario)
calcula_imposto_renda(valor_salario)