nume1: int = 0
total: int = 0

while True:
    nume1 = int(input("digite um numero: "))
    if nume1 < 0: 
        break
    total = total + nume1
print("a soma total foi: ", total)