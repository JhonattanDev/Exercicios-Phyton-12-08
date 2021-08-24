import random


def main():
    print("*************************************")
    print("  Bem vindo ao jogo de Adivinhação!  ")
    print(" Tente adivinhar o número de 1 a 100 ")
    print("*************************************")

    numero_secreto = random.randint(1, 100)
    total_de_tentativas = 10

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = int(input('Digite um número de 1 a 100: '))

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print('Você acertou!')
            break
        else:
            if(maior):
                print('Você errou! O seu chute foi maior que o número secreto.')
            elif(menor):
                print('Você errou! O seu chute foi menor que o número secreto.')

        if (rodada == total_de_tentativas):
            print("Acabaram as chances, o número secreto era {}.".format(numero_secreto))


if(__name__ == "__main__"):
    main()
