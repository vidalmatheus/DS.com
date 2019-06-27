import os,psycopg2
import datetime
import bcrypt

class MicroData():
    def __init__(self):
        pass


class PessoaUserData(MicroData):
    def __init__(self):
        #self.dictionaryInfo = {'name':"visitante", 'logged': False, 'birthDate':datetime.datetime.now(),
        #                       'hasSaram':False,'saram':0000000}

        super(PessoaUserData, self).__init__()
        self.name = "visitante"
        self.cpf = "0000000"
        self.saram = ""
        self.dataNascimento = datetime.datetime.now()
        self.possuiSaram = False
        self.endereco = ""
        self.numContato = ""
        self.email = ""
        self.sexo = ""
        self.classificacao = ""
        self.confirmado = False

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

    def setUser(self,listaTupleUser):
        self.cpf = listaTupleUser[0]
        self.saram = listaTupleUser[2]
        self.name = listaTupleUser[3]
        self.dataNascimento = listaTupleUser[4]
        self.sexo = listaTupleUser[5]
        self.endereco = listaTupleUser[6]
        self.numContato = listaTupleUser[7]
        self.email = listaTupleUser[8]
        self.classificacao = listaTupleUser[9]
        self.confirmado = listaTupleUser[10]


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


#Permite o armazenamento e manipulação dos dados do medico
class MedicoUserData(MicroData):
    def __init__(self):
        #self.dictionaryInfo = {'name':"visitante", 'logged': False, 'birthDate':datetime.datetime.now(),
        #                       'hasSaram':False,'saram':0000000}
        super(MedicoUserData , self).__init__()
        self.name = "visitante"
        self.cpf = "0000000"
        self.saram = ""
        self.militar = ""
        self.crm = "00000000"
        self.especialidade = "medico"

    def getCPF(self):
        return self.cpf

    def getName(self):
        return self.name

    def getSaram(self):
        return self.saram

    def getCRM(self):
        return self.crm

    def getEspecialidade(self):
        return self.especialidade

    def setUser(self,listaTupleUser):
        self.cpf = listaTupleUser[0]
        self.saram = listaTupleUser[2]
        self.name = listaTupleUser[3]
        self.militar = listaTupleUser[4]
        self.crm = listaTupleUser[5]
        self.especialidade = listaTupleUser[6]

    def getStringListName(self):
        return ["Nome", "saram", "cpf", "militar", "crm", "especialidade"]

    def getStringList(self):
        lista = []
        lista.append(self.name)
        lista.append(str(self.saram))
        lista.append(self.cpf)
        lista.append(self.militar)
        lista.append(self.crm)
        lista.append(self.especialidade)
        return lista


#Manipula o banco de dados e acessa
class DataManager:
    def __init__(self):
        DATABASE_URL = os.environ['DATABASE_URL']
        self.dataConnection = psycopg2.connect(DATABASE_URL, sslmode='require')

    def __del__(self):
        self.dataConnection.close()
    
    def getConnector(self):
        return self.dataConnection

    def __getDataType__(self, dataType = "paciente",dataName = "saram",dataVar = "0"):
        print('\n//////////////////////////////////////////////////////////////////////////')
        print("DataManager __getDataType__ comeca")
        cursor = self.dataConnection.cursor()
        achou = True
        cursor.execute("SELECT * FROM "+dataType+" WHERE "+dataName+" = %s", (dataVar,))
        user = cursor.fetchall()
        cursor.close()
        print("DataManager __getDataType__ acaba")
        print('//////////////////////////////////////////////////////////////////////////\n')
        if len(user) == 0: achou = False
        return achou, user

    def confirmPessoaPassword(self,dataType = "paciente",dataName = "saram",dataVar = "0",password = ""):
        print('\n//////////////////////////////////////////////////////////////////////////')
        print("DataManager confirmPacientePassword comeca")
        dataExist = False
        passWordCorrect = False
        pessoaData = MicroData()
        dataExist, user = self.__getDataType__(dataType,dataName ,dataVar)

        print("o tipo de variavel da user[0] = " + str(type(user[0])))
        print("o tipo de variavel da user[0][0] = " + str(type(user[0][0])))
        print("o tipo de variavel da user[0][1] = " + str(type(user[0][1])))
        print("o tipo de variavel da user[0][2] = " + str(type(user[0][2])))
        print("o tipo de variavel da user[0][3] = " + str(type(user[0][3])))
        print("o tipo de variavel da user[0][4] = " + str(type(user[0][4])))
        print("o tipo de variavel da user[0][5] = " + str(type(user[0][5])))
        print("o tipo de variavel da user[0][6] = " + str(type(user[0][6])))
        print("o tipo de variavel da user[0][7] = " + str(type(user[0][7])))
        print("o tipo de variavel da user[0][8] = " + str(type(user[0][8])))
        print("o tipo de variavel da user[0][9] = " + str(type(user[0][9])))
        print("o user[0][9] = " + user[0][9])
        print("o tipo de variavel da user[0][10] = " + str(type(user[0][10])))
        if dataExist:
            passworDataBase = user[0][1]
            passWordCorrect = (bcrypt.hashpw(password.encode(),passworDataBase.encode())==passworDataBase.encode())
            if passWordCorrect:
                if dataType == "paciente":
                    pessoaData = PessoaUserData()
                    pessoaData.setUser(user[0])
                elif dataType == "medico":
                    pessoaData = MedicoUserData()
                    pessoaData.setUser(user[0])

        #tuplaResposta = (dataExist,passWordCorrect,pacienteData)
        print("\nDataManager confirmPacientePassword acaba")
        print('//////////////////////////////////////////////////////////////////////////\n')
        return dataExist,passWordCorrect,pessoaData

    def getExecute(self,command = "SELECT distinct especialidade FROM medico ORDER BY especialidade",tupla = ()):
        cursor = self.dataConnection.cursor()
        if len(tupla) == 0:
            cursor.execute(command)
        else:
            cursor.execute(command,tupla)

        data = cursor.fetchall()
        cursor.close()
        return data

    def getDataInfo(self,dataType = "paciente",dataName = "saram",dataVar = "0"):
        print('//////////////////////////////////////////////////////////////////////////')
        print("DataManager getPacienteInfo comeca")
        print("getDataInfo")
        if (len(dataVar) == 11 and dataName == "cpf"):
            dataVar = dataVar[0:3] + "." + dataVar[3:6] + "." + dataVar[6:9] + "-" + dataVar[9:11]
        pessoasDatas = []
        dataExist, tupla = self.__getDataType__(dataType,dataName, dataVar)


        print("DataManager getPacienteInfo acaba")
        print('//////////////////////////////////////////////////////////////////////////\n')
        return dataExist, tupla

    def verificaSeContaEstaLogadaReLogada(self, sessionHash, sessionCPF,userType):
        foiRelogado = False
        estaLogado = False
        tupla = self.__getDataType__("usuariosLogado", "cpf" , sessionCPF)
        estaLogado = tupla[0]
        usuario = tupla[1]
        if estaLogado:
            foiRelogado = not ("verificaSeOSessionHashEdiferrente"=="verificaSeOSessionHashEdiferrente")

        return estaLogado, foiRelogado

    def normalizeCPF(self,dataCpf):
        normalizedCPF = dataCpf
        if (len(dataCpf) == 11):
            normalizedCPF = dataCpf[0:3] + "." + dataCpf[3:6] + "." + dataCpf[6:9] + "-" + dataCpf[9:11]
        elif (len(dataCpf) == 14):
            print("CPF JA NORMALIZADO\n")
        else:
            print("CPF NAO VALIDO\n")
        return normalizedCPF

    def deleteDataType(self,dataType = "logado"):
        cursor = self.dataConnection.cursor()
        cursor.execute("TRUNCATE TABLE "+ dataType)
        self.dataConnection.commit()

    def changeDataAndReturnNewData(self, dataType, dataStringList, dataVarList,dataLookVar,dataLook = "saram"):
        if (len(dataLookVar) == 11 and dataLook == "cpf"):
            dataLookVar = dataLookVar[0:3] + "." + dataLookVar[3:6] + "." + dataLookVar[6:9] + "-" + dataLookVar[9:11]
        cursor = self.dataConnection.cursor()
        tuplaValues = ()
        comandoString = "UPDATE " + dataType + " SET "
        n = len(dataStringList)
        i = 1
        comandoString = comandoString + dataStringList[0] + "=%s"
        tuplaValues = (dataVarList[0],)
        while i < n:
            comandoString = comandoString + "," +dataStringList[i] + "=%s"
            tuplaValues = tuplaValues + (dataVarList[i],)
            i = i + 1

        comandoString = comandoString + " WHERE " + dataLook + "=%s"
        tuplaValues = tuplaValues + (dataLookVar,)

        if n > 0:
            cursor.execute(comandoString, tuplaValues)
            print("ATUALIZAÇÃO DOS DADOS COM SUCESSO\n")
        else:
            print("NAO FOI DETERMINADO VALORES PARA MUDAR\n")

        self.dataConnection.commit()

        cursor.execute("SELECT * FROM "+dataType+ " WHERE "+dataLook +" = %s", (dataLookVar,))
        newData = cursor.fetchall()
        cursor.close()
        return newData

    def addDataThenGetIt(self, dataType, dataVarList):
        cursor = self.dataConnection.cursor()
        tuplaValues = ()
        comandoString = "INSERT INTO " + dataType + " VALUES(%s"
        n = len(dataVarList)
        i = 1

        tuplaValues = (dataVarList[0],)
        while i < n:
            comandoString = comandoString + ", %s"
            tuplaValues = tuplaValues + (dataVarList[i],)
            i = i + 1

        comandoString = comandoString + ")"

        if n > 0:
            cursor.execute(comandoString, tuplaValues)
            print("ATUALIZACAO DOS DADOS COM SUCESSO\n")
        else:
            print("NAO FOI DETERMINADO VALORES PARA MUDAR\n")

        self.dataConnection.commit()
        cursor.close()
        return tuplaValues

    def deleteData(self, dataType, dataLookVar,dataLook = "saram"):
        cursor = self.dataConnection.cursor()
        cursor.execute("DELETE FROM " + dataType + " WHERE " + dataLook + " = %s", (dataLookVar,))


        cursor.close()

        self.dataConnection.commit()

    def getAllInfoDataType(self, dataType = 'paciente'):
        cursor = self.dataConnection.cursor()
        cursor.execute("SELECT * FROM " + dataType)
        dataInfoTuple = cursor.fetchall()
        cursor.close()

        return dataInfoTuple

