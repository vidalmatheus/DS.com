from sharedData import *
login_api = Blueprint('login_api', __name__)

#login
@login_api.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        psd = userDetails['password']
        #cursor
        cur = connectionData.getConnector().cursor()
        errorSARAM = errorCPF = False
        if (len(userDetails['login']) == 7 or len(userDetails['login']) == 11):
            if (len(userDetails['login']) == 7):
                saram = userDetails['login']
                cur.execute("SELECT * FROM paciente WHERE saram = %s",(saram,))
                user = cur.fetchall()
                if (len(user)==0): errorSARAM = True
            elif (len(userDetails['login']) == 11):
                cpf = userDetails['login']
                #134.202.967-46
                cpf = cpf[0:3]+"."+cpf[3:6]+"."+cpf[6:9]+"-"+cpf[9:11]
                print(cpf)
                cur.execute("SELECT * FROM paciente WHERE cpf = %s",(cpf,))
                user = cur.fetchall()
                if (len(user)==0): errorCPF = True

            if (errorSARAM): print("SARAM NÃO ENCONTRADO")
            elif (errorCPF): print("CPF NÃO ENCONTRADO")
            else:
                psd_db = user[0][1]
                print("o tipo de variavel da user[0] é "+str(type(user[0])))
                print("o tipo de variavel da user[0][0] é " + str(type(user[0][0])))
                print("o tipo de variavel da user[0][1] é " + str(type(user[0][1])))
                print("o tipo de variavel da user[0][2] é " + str(type(user[0][2])))
                print("o tipo de variavel da user[0][3] é " + str(type(user[0][3])))
                print("o tipo de variavel da user[0][4] é " + str(type(user[0][4])))
                print("o tipo de variavel da user[0][5] é " + str(type(user[0][5])))
                print("o tipo de variavel da user[0][6] é " + str(type(user[0][6])))
                print("o tipo de variavel da user[0][7] é " + str(type(user[0][7])))
                print("o tipo de variavel da user[0][8] é " + str(type(user[0][8])))
                print("o tipo de variavel da user[0][9] é " + str(type(user[0][9])))
                print("o tipo de variavel da user[0][10] é " + str(type(user[0][10])))
                #vou alterar umas coisas aqui

                userData.logginUser(user[0])

                #fim alteração
                print(bcrypt.hashpw(psd.encode(),psd_db.encode()))
                print(psd_db.encode())
                if (bcrypt.hashpw(psd.encode(),psd_db.encode()) == psd_db.encode()):
                    #close the cursor
                    cur.close()
                    #return redirect(url_for('logged_api.logged',userDetails=user[0][3])) ### FALTA PASSAR ALGUM PARÂMETRO PARA SABER O NOME ###
                    return redirect('/logged')
                else: print("SENHA ERRADA!") ## FALTA JOGAR PRO html
        else: print("ERRO! CPF OU SENHA EM FORMATO INCORRETO!") ## FALTA JOGAR PRO html

    return render_template('login.html')
