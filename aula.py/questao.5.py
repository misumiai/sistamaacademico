num1: int = int(input("informe o numero: "))
contador: int = 0 

while contador <= 10:
    tabuada: int = num1 * contador
    print(f"tabuada de {num1} X {contador} é {tabuada}")
    contador = contador + 1

