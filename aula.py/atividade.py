figura = input(("C = circulo; Q = quadrado; R = retangulo: "))

if figura == "C":
    r = float(input("raio: "))
    print("Área:", 3.14 * (r ** 2))
elif figura == "Q":
    l = float(input("lado: "))
    print("Área:", l * (l ** 2))
elif figura == "R":
    b = float(input("base: "))
    h = float(input("altura: "))
    print("Área:", b * h)
else:
    print("opção invalida")