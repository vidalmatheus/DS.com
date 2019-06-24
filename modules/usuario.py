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

    def copy(self, userCopied):
        self.name = userCopied.name
        self.logado = userCopied.logado
        self.cpf = userCopied.cpf
        self.dataNascimento = userCopied.dataNascimento
        self.saram = userCopied.saram
        self.endereco = userCopied.endereco
        self.numContato = userCopied.numContato
        self.email = userCopied.email
        self.sexo = userCopied.sexo
        self.classificacao = userCopied.classificacao
        self.confirmado = userCopied.confirmado


class acessManager:
    def __init__(self):
        self.dictUsersOn = {"0000000" : acessoUser()}
    def resetServer(self):
        self.dictUsersOn.clear()
        self.dictUsersOn = {"0000000" : acessoUser()}
    def addUserOn(self, user = acessoUser()):
        cpf = user.getCPF()
        userDict = acessoUser()
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
        
        userDict.copy(user)
        self.dictUsersOn.update({cpf: userDict})
        print("self.dictUsersOn[cpf].getStringList() = " + str(self.dictUsersOn[cpf].getStringList()))

    def logoutUser(self,cpf):
        print("/////////////////////////////////")
        print("logout user")
        if not self.dictUsersOn:
            print("self.dictUsersOn is empty")
            return
        if cpf in self.dictUsersOn:
            print("cpf in self.dictUsersOn")
            print("self.dictUsersOn[cpf].getStringList() = " + str(self.dictUsersOn[cpf].getStringList()))
            print("self.dictUsersOn = " + str(self.dictUsersOn))
            self.dictUsersOn.clear()
            self.dictUsersOn = {"0000000" : acessoUser()}
            #self.dictUsersOn.pop(cpf, None)
            print("self.dictUsersOn = " + str(self.dictUsersOn))
        print("ended logoutUser()")

    def userIsOn(self,cpf):
        isOnDict = (cpf in self.dictUsersOn)
        print("/////////////////////////////")
        print("acessManager.userIsOn()")
        if isOnDict:
            print("User is on       ?")
            print("self.dictUsersOn = "+ str(self.dictUsersOn))
            if self.dictUsersOn[cpf] == None:
                return False
            return True

        return False

    def getDictionary(self):
        return self.dictUsersOn

    def getUser(self,cpf):
        print("/////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("getUser")
        print("tipo de cpf = " + str(type(cpf)))
        dataReturn = acessoUser()
        print("cpf = " + cpf)
        print("self.dictUsersOn = " + str(self.dictUsersOn))
        if cpf in self.dictUsersOn:
            print("tipo de self.dictUsersOn[cpf] = " + str(type(self.dictUsersOn[cpf])))
            dataReturn.copy(self.dictUsersOn[cpf])
            print("dataReturn.getStringList = "+str(dataReturn.getStringList))
            print
            return dataReturn
        else:
            print("return None")
            return None
