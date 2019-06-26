#from sharedData import *
from flask import render_template, request, redirect,Blueprint, session
import bcrypt, datetime
from modules import dataBase
login_api = Blueprint('login_api', __name__)

#login
@login_api.route("/login", methods=['GET', 'POST'])
def login():
    userData = dataBase.PessoaUserData()
    baseData = dataBase.DataManager()
    loginType = ""
    #verifica se session is correct


    if "userCPF" in session:
        if "verifica se esta loggado com o 'loginHash' correto"=="verifica se esta loggado com o 'loginHash' correto":
            #session["loginHash"]
            #session["userName"] = userData.getName()
            #session["userCPF"]
            if session["userType"] == 'P':
               cpf = session['userID']
            elif session["userType"] == 'M':
                crm = session['userID']
            return redirect('/logged')
        else:
            session.pop("loginHash", None)
            session.pop("userName", None)
            session.pop("userID", None)
            session.pop("userType", None)


    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        passWord = userDetails['password']

        errorSARAM = errorCPF = False
        if (len(userDetails['login']) == 7 or len(userDetails['login']) == 11):
            if (len(userDetails['login']) == 7):
                loginType = "saram"
            elif (len(userDetails['login']) == 11 or len(userDetails['login']) == 14):
                loginType = "cpf"
                cpf = userDetails['login']

            #pega as informaçoes
            dataExist,passwordCorrect,userData = baseData.confirmPessoaPassword("paciente", loginType, userDetails['login'],passWord)

            if not dataExist:
                dataExist, passwordCorrect, userData = baseData.confirmPessoaPassword("medico", loginType,
                                                                                      userDetails['login'], passWord)

            if not dataExist:
                print("SARAM/CPF NAO ENCONTRADO")
                return redirect('/login')
            else:
                if passwordCorrect:
                    session["userName"] = userData.getName()
                    session["userID"] = userData.getCPF()
                    session["loginHash"] = bcrypt.hashpw((userData.getName()+userData.getCPF()+str(datetime.datetime.now())).encode(),bcrypt.gensalt(12)).decode('utf-8')
                    session["userType"] = "P"

                    #muda em logged in database

                    return redirect('/logged')

                else:
                    print("SENHA ERRADA")
                    return redirect('/login')


        else: print("ERRO! CPF OU SENHA EM FORMATO INCORRETO!") ## FALTA JOGAR PRO html

    return render_template('login.html')
