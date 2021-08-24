import random


def main():
    def continuar():
        print('Escolha uma palavra para continuar!')

    def adivinhar():
        palavra_sorteada = random.randint(0, 99)

        resposta = input('A palavra escolhida foi {}? (S / N): '.format(lista[palavra_sorteada]))
        resposta = resposta.strip()

        if (resposta.upper() == 'S'):
            print("Eu acertei :)")
            jogar_denovo()
        else:  # N
            print("Eu errei :(")
            adivinhar()

    def jogar_denovo():
        jogar_novamente = input("Deseja jogar novamente? (S / N): ")
        jogar_novamente = jogar_novamente.strip()

        if(jogar_novamente.upper() == 'S'):
            inicio()
        else:  # N
            print("Obrigado por jogar :)")

    def inicio():
        iniciar = input("Já escolheu a palavra? Podemos começar? (S / N): ")
        iniciar = iniciar.strip()

        if(iniciar.upper() == 'S'):
            adivinhar()
        else:  # N
            continuar()
            inicio()

    print("*****************************************************")
    print("Escolha uma palavra para o programa tentar adivinhar!")
    print("*****************************************************")

    lista = ['Ministro', 'Reboque', 'Gravata', 'Zoológico', 'Ferradura',
             'Carretel', 'Privada', 'Ferreiro', 'Gladiador', 'Duplicar',
             'Palma', 'Perpendicular', 'Astrologia', 'Soco', 'Tinta',
             'Amuleto', 'Cereais', 'Almanaque', 'Antro', 'Cabeleireiro',
             'Estrada', 'Bailarina', 'Molde', 'Tabuleta', 'Cubo',
             'Alface', 'Ninja', 'Kiwi', 'Futuro', 'Madri',
             'Derrota', 'Pegar', 'Assunto', 'Altura', 'Peludo',
             'Furacão', 'Verruga', 'Chaleira', 'Tempo', 'Plantas',
             'Adulto', 'Declarar', 'Enteada', 'Encontro', 'Direito',
             'Poluir', 'Tambor', 'Fechado', 'Lesma', 'Vocal',
             'Maiô', 'Janeiro', 'Barulhento', 'Soldados', 'Cereal',
             'Consoantes', 'Sombra', 'Ofensa', 'Puberdade', 'Mulher',
             'Spray', 'Mansão', 'Inocente', 'Inferno', 'Ponta',
             'Transbordar', 'Aldeia', 'Disputa', 'Panda', 'Camisa',
             'Compartimento', 'Julgamento', 'Costureira', 'Galo', 'Rastejar',
             'Tio', 'Semanas', 'Apoio', 'Andares', 'Jaguar',
             'Vizinhos', 'Peru', 'Alface', 'Radical', 'Noiva',
             'Abóbora', 'Integral', 'Bruto', 'Colocar', 'Maca',
             'Aspirina', 'Chuveiro', 'Pinos', 'Cortina', 'Amputar',
             'Foguete', 'Vinagre', 'Jovem', 'Capacete', 'Madri']

    for i in range(len(lista)):
        print(lista[i])

    print("****************************************************************")
    print("Escolha uma das palavras acima para o programa tentar adivinhar!")
    print("****************************************************************")
    print("Por favor, responda com S (Sim) ou N (Não).")

    inicio()


if(__name__ == "__main__"):
    main()
