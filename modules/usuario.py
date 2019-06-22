class acessoUser:
    def __init__(self):
        self.name = "visitante"
        self.logado = False
        self.cpf = ""
        self.dataNascimento = ""
        self.saram = ""
        self.endereco = ""
        self.numContato = ""
        self.email = ""
        self.sexo = ""
        self.alunoITA = False
        self.confirmado = False

    def loggedUser(self,listaStringUser):
        self.cpf = listaStringUser[0]
        self.logado = True
        self.saram = listaStringUser[2]
        self.name = listaStringUser[3]
        self.dataNascimento = listaStringUser[4]
        self.sexo = listaStringUser[5]
        self.endereco = listaStringUser[6]
        self.numContato = listaStringUser[7]
        self.email = listaStringUser[8]
        self.alunoITA = (listaStringUser[9] == "True")
        self.confirmado = (listaStringUser[10] == "True")

