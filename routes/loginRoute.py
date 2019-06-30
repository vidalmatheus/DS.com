from sharedData import *


login_api = Blueprint('login_api', __name__)

#login
@login_api.route("/login", methods=['GET', 'POST'])
def login():
    global usersDataOnline
    alert=""
    print("////////////////////////////////////////")
    print("Comeca route login")
    print("usersDataOnline.dictUsersOn = "+str(usersDataOnline.dictUsersOn))
    userData = usuario.acessoUser()
    if 'user' in session:
        print("user is in session")
        if usersDataOnline.userIsOn(session['user']):
            print("Usuario ira loggar")
            return redirect('/logged')
        else:
            print("user saira de session")
            session.pop('user', None)
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
                cpf = cpf[0:3]+"."+cpf[3:6]+"."+cpf[6:9]+"-"+cpf[9:11]
                cur.execute("SELECT * FROM paciente WHERE cpf = %s",(cpf,))
                user = cur.fetchall()
                if (len(user)==0): errorCPF = True
            if (errorSARAM): alert = "SARAM não encontrado. Efetuar cadastro."
            elif (errorCPF): alert = "CPF não encontrado. Efetuar cadastro."
            else:
                psd_db = user[0][1]
                print("o tipo de variavel da user[0] = "+str(type(user[0])))
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
                #vou alterar umas coisas aqui
                #fim alteração
                if (bcrypt.hashpw(psd.encode(),psd_db.encode()) == psd_db.encode()):
                    userData.logginUser(user[0])
                    print("userData.getStringList() = "+str(userData.getStringList()))
                    if 'user' in session:
                        print("session['user'] = "+str(session['user']))

                    print("usersDataOnline.dictUsersOn = "+str(usersDataOnline.dictUsersOn))
                    if usersDataOnline.userIsOn(userData.getCPF()):
                        print("Ja esta logada!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        usersDataOnline.logoutUser(session['user'])
                        session.pop('user', None)
                        #return redirect('/login')
                    
                    print("Usuario nao esta logado")
                    session['user'] = userData.getCPF()
                    usersDataOnline.addUserOn(userData)
                    print("dicionary of user = "+ str(usersDataOnline.getDictionary()))
                    print("fAZ Login")
                    print("FLAG 13")
                    #close the cursor
                    cur.close()
                    #return redirect(url_for('logged_api.logged',userDetails=user[0][3])) ### FALTA PASSAR ALGUM PARÂMETRO PARA SABER O NOME ###
                    return redirect('/logged')
                else: alert = "Senha incorreta. Tente novamente!" ## FALTA JOGAR PRO html
        else: alert = "ERRO! SARAM/CPF em formato incorreto!" ## FALTA JOGAR PRO html
    print(alert)
    return render_template('login.html',alert=alert)
