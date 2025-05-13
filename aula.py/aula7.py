print("Notas")
nota: float = float(input("Digite sua nota aqui: "))

if nota >= 6.0:
   print("aprovado");
elif nota <= 4.0:
   print("o aluno esta reprovado")
else:
   print("o aluno esta de recuperação")