import datetime


class acessoUser:
    def __init__(self):
        self.name = "visitante"
        self.logado = False
        self.cpf = "0000000"
        self.dataNascimento = datetime.datetime.now()
        self.saram = 0000000
        self.endereco = ""
        self.numContato = ""
        self.email = ""
        self.sexo = ""
        self.classificacao = ""
        self.confirmado = False

    def getLogged(self):
        return self.logado
    def getCPF(self):
        return self.cpf

    def getNumContato(self):
        return self.numContato

    def getName(self):
        return self.name

    def getSaram(self):
        return self.saram

    def getEmail(self):
        return self.email

    def getDataNascimento(self):
        return self.dataNascimento

    def getEndereco(self):
        return self.endereco

    def isConfirmed(self):
        return self.confirmado

    def getSexo(self):
        if self.sexo == "M" or self.sexo == "m":
            return "Masculino"
        elif self.sexo == "F" or self.sexo == "f":
            return "Feminino"

        return ""

    def logginUser(self,listaTupleUser):
        self.cpf = listaTupleUser[0]
        self.logado = True
        self.saram = listaTupleUser[2]
        self.name = listaTupleUser[3]
        self.dataNascimento = listaTupleUser[4]
        self.sexo = listaTupleUser[5]
        self.endereco = listaTupleUser[6]
        self.numContato = listaTupleUser[7]
        self.email = listaTupleUser[8]
        self.classificacao = listaTupleUser[9]
        self.confirmado = listaTupleUser[10]

    def logOutUser(self):
        self.name = "visitante"
        self.logado = False
        self.cpf = ""
        self.dataNascimento = datetime.datetime.now()
        self.saram = 0000000
        self.endereco = ""
        self.numContato = ""
        self.email = ""
        self.sexo = ""
        self.classificacao = ""
        self.confirmado = False

    def getStringList(self):
        lista = []
        lista.append(self.name)
        lista.append(str(self.saram))
        lista.append(self.cpf)
        lista.append(str(self.dataNascimento))
        lista.append(self.sexo)
        lista.append(self.endereco)
        lista.append(self.numContato)
        lista.append(self.email)
        lista.append(self.classificacao)
        return lista


class acessManager:
    def __init__(self):
        self.dictUsersOn = {"0000000" : acessoUser()}

    def addUserOn(self, user = acessoUser()):
        if user.getCPF() == "0000000":
            return
        self.dictUsersOn.update({user.getCPF(): user})

    def logoutUser(self,cpf):
        self.dictUsersOn.pop(str(cpf), None)

    def getUser(self,cpf):
        return self.dictUsersOn[str(cpf)]
