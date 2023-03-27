print("**********************************")
print("Bem vindo no jogo de Adivinhação")
print("**********************************")

numero_secreto = 42

chute_string = input("Digite o seu número: ")

print("Você  digitou ", chute_string)

chute = int(chute_string)

acertou = (numero_secreto == chute)

if (acertou):
    print("Você acertou")
else:
    if (chute > numero_secreto):
        print("Voce errou! O seu chute foi maior do que o número secreto.")
    elif (chute < numero_secreto):
        print("Você errou! O seu chute foi menor do que o número secreto.")
print("Fim de Jogo!")