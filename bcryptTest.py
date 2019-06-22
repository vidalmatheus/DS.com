import bcrypt


if __name__== "__main__":
    password = '123456'
    passwordTry = '123456'

    #pega o hash
    hashed_password = bcrypt.hashpw(password.encode(),bcrypt.gensalt(12))

    #comparação abaixo:
    correto = (bcrypt.hashpw(passwordTry.encode(),hashed_password)==hashed_password)

    print(hashed_password)
    print(bcrypt.hashpw(passwordTry.encode(),hashed_password))

    print("Verificacao de password = " + str(correto))
    print("versao de bcrypt = "+bcrypt.__version__)

