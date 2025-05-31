def quadrado():
  base: int = int(input("informe o base: "))
  altura: int = int(input("informe o altura: "))

  total: int = base * altura
  print("O total do quadrado é: ", total)

def triangulo():
  base: int = int(input("informe a base: "))
  altura: int = int(input("informe a altura: "))

  total: int = base * altura / 2
  print("O total do triangulo é: ", total)

def retangulo():
  base: int = int(input("informe o base: "))
  altura: int = int(input("informe o altura: "))

  total: int = base * altura
  print("O total do retangulo é: ", total)

def circulo():
  raio: float = float(input("informe o raio: "))
  pi: float = 3.14

  total: int = pi * (raio ** 2)
  print("O total do circulo é: ", total)

quadrado()
triangulo()
retangulo()
circulo()
