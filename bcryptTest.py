import bcrypt


if __name__== "__main__":
    password = '123456'
    passwordTry = '1234567'

    #pega o hash
    hashed_passwordNodecode = bcrypt.hashpw(password.encode(),bcrypt.gensalt(12))
    hashed_password = hashed_passwordNodecode.decode('utf-8')
    #hashed_passwordNodecode = bcrypt.generate_password_hash(password)
    #hashed_password = hashed_passwordNodecode.decode('utf-8')

    #comparação abaixo:
    correto = (bcrypt.hashpw(passwordTry.encode(),hashed_password.encode())==hashed_password.encode())
    #correto = bcrypt.check_password_hash(user.password, form.password.data)

    #print("noDecode = " + hashed_passwordNodecode )
    print("noDecode = " + str(hashed_passwordNodecode))

    print("Decode = " + hashed_password)
    print("DecodeToEncode = " + str(hashed_password.encode()))

    print("Verificacao de password = " + str(correto))
    print("versao de bcrypt = "+bcrypt.__version__)

