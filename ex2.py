def main():
    email = input('Digite o seu email: ')  # jhonattan@gmail.com
    email = email.split('@')  # ['jhonattan', 'gmail.com']

#    print(email[0])  # jhonattan
#    print(email[1])  # gmail.com

    usuario = email[0].capitalize()
    dominio = email[1]

#    print(usuario)  # Jhonattan
#    print(dominio)  # gmail.com

    print('Seja bem-vindo, {}, o seu e-mail é de domínio {}.'.format(usuario, dominio))


if(__name__ == "__main__"):
    main()
