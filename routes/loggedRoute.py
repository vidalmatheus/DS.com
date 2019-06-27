from sharedData import session, dataBase
from flask import Flask, render_template, request, redirect,Blueprint, json, url_for
from modules import dataBase
import sharedData
import time

logged_api = Blueprint('logged_api', __name__)


# logged page
@logged_api.route('/logged', methods=['GET'])
def logged():
    print("/////////////////////////////\nCOMECA LOGGED")
    start = time.time()
    baseData = dataBase.DataManager()
    loginType = ""
    # verifica se session is correct

    # trabalha com a sessão e verifica se esta logado

    if "userID" in session:
        cpf = session['userID']
        dataName = "cpf"

        dataAchou, tupleLogado = baseData.getDataInfo("logado", dataName, session['userID'])

        if dataAchou:
            dataAchou = (tupleLogado[0][1] == session['loginHash'])

            if dataAchou:
                if session['userType'] == 'M':
                    return redirect('/loggedMedicos')

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

    print(request.args.get('userDetails'))
    #userData = usersDataOnline.getUser(session['user'])
    if not "verifica no banco de dados se esta logado" == "verifica no banco de dados se esta logado":
        print("SE TIVER EM SESSION MAS NAO ESTA NO BANCO DE LOGADOS")


        session.pop("loginHash", None)
        session.pop("userName", None)
        session.pop("userCPF", None)
        session.pop("userType", None)

        return redirect('/login')

    print("RENDERIZA A TELA DE LOGGED")
    return render_template('logged.html', userDetails = session['userName'])

