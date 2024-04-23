from random import randint
print("Escolha um numero de 1 a 30")
winner = randint(1,30)
value = 0
while value != winner:
        value = int(input(" -> : "))
        if value == winner:
                print("O valor : ",  winner," foi sorteado \n")
                print("-" * 30)
                print("++++ VENCEU ++++", "\n", " +++ ",winner," +++")

        if value > 30:
                print("Escolha um valor menor que 30")
        if value < 0:
                print("Escolha um valor maior que 0")
