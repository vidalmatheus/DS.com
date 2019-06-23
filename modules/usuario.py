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
        cpf = user.getCPF()
        print("cpf = " + str(cpf))
        print("///////////////////////")
        print("Entrou Add User")
        if cpf == "0000000":
            print("return 01")
            return
        if cpf in self.dictUsersOn:
            print("return 02")
            self.dictUsersOn[user.getCPF()] = user
            print("user.getStringList() = " + str(user.getStringList()))
            return
        
        self.dictUsersOn.update({cpf: user})
        print("self.dictUsersOn[cpf].getStringList() = " + self.dictUsersOn[cpf].getStringList())

    def logoutUser(self,cpf):
        if cpf == "0000000" and self.dictUsersOn != None:
            return
        if cpf in self.dictUsersOn:
            self.dictUsersOn.pop(cpf, None)

    def userIsOn(self,cpf):
        isOnDict = (cpf in self.dictUsersOn)
        print("/////////////////////////////")
        print("acessManager.userIsOn()")
        if isOnDict:
            print("User is on       ?")
            print(str(self.dictUsersOn))
            if self.dictUsersOn[cpf] == None:
                return False
            return True

        return False

    def getDictionary(self):
        return self.dictUsersOn

    def getUser(self,cpf):
        print("/////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("tipo de cpf = " + str(type(cpf)))
        print("cpf = " + cpf)
        print("self.dictUsersOn = " + str(self.dictUsersOn))
        if cpf in self.dictUsersOn:
            print("tipo de self.dictUsersOn[cpf] = " + str(type(self.dictUsersOn[cpf])))
            return self.dictUsersOn[cpf]
        else:
            return None
