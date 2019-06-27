from sharedData import session
from flask import render_template, request, redirect,Blueprint
import bcrypt, datetime
from modules import dataBase
import sharedData
loginMedico_api = Blueprint('loginMedico_api', __name__)

#login
@loginMedico_api.route("/loginMedico", methods=['GET', 'POST'])
def login():
    userData = dataBase.PessoaUserData()
    #baseData = sharedData.baseData
    baseData = dataBase.DataManager()
    loginType = ""
    #verifica se session is correct

    #trabalha com a sessão e verifica se esta logado

    if "userID" in session:
        cpf = session['userID']
        dataName = "cpf"

        dataAchou, tupleLogado = baseData.getDataInfo("logado", dataName, session['userID'])

        if dataAchou:
            dataAchou = (tupleLogado[0][1] == session['loginHash'])

            if dataAchou:
                if session['userType'] == 'P':
                    return redirect('/logged')
                elif session['userType'] == 'M':
                    return redirect('/loggedMedico')

        if not dataAchou:
            session.pop("loginHash", None)
            session.pop("userName", None)
            session.pop("userID", None)
            session.pop("userType", None)
    else:
        session.pop("loginHash", None)
        session.pop("userName", None)
        session.pop("userID", None)
        session.pop("userType", None)

    # caso esteja apropridamente logado continua

    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        passWord = userDetails['password']
        alert = ""
        errorSARAM = errorCPF = False
        if (len(userDetails['login']) == 8):
            loginType = "crm"
            crm = userDetails['login']

            #pega as informaçoes
            dataExist,passwordCorrect,userData = baseData.confirmPessoaPassword("medico", loginType, userDetails['login'],passWord)

            print("/////////////////////////////\nverifica senha")

            #######################VERIFICA SE ADCIONA NO LOGADO
            if not dataExist:
                alert = "ERRO! CRM NAO ENCONTRADO!" ## FALTA JOGAR PRO html
                #return redirect('/login')
            else:
                print("DATA EXIST")
                if passwordCorrect:
                    print("PASSWORD IS CORRECT")
                    session["userName"] = userData.getName()
                    session["userID"] = userData.getCPF()
                    session["loginHash"] = bcrypt.hashpw((userData.getName()+userData.getCPF()+str(datetime.datetime.now())).encode(),bcrypt.gensalt(12)).decode('utf-8')
                    session["userType"] = "M"

                    ########VERIFICA SE ESTA NO LOGADO E RETIRA, PARA DEPOIS O POR DE VOLTA

                    dataAchou, tupleLogado = baseData.getDataInfo("logado", "cpf", session['userID'])
                    
                    if dataAchou:
                        user = baseData.changeDataAndReturnNewData("logado",
                                                                   ['session_hash'], [session["loginHash"]], session["userID"], 'cpf')
                    else:
                        tupleData = baseData.addDataThenGetIt("logado", (userData.getCPF(), session["loginHash"]))
                    ########VERIFICA SE ESTA NO LOGADO E TROCA

                    #muda em logged in database

                    return redirect('/loggedMedico')

                else:
                    alert = "Senha incorreta. Tente novamente!" ## FALTA JOGAR PRO html
                    #return redirect('/login')


        else: print("ERRO! CPF OU SENHA EM FORMATO INCORRETO!") ## FALTA JOGAR PRO html

        print(alert)

    return render_template('loginMedico.html')
