from sharedData import session
from flask import Flask, render_template, request, redirect,Blueprint, json, url_for
from modules import dataBase


logged_api = Blueprint('logged_api', __name__)


# logged page
@logged_api.route('/logged', methods=['GET'])
def logged():
    print("/////////////////////////////\nCOMECA LOGGED")

    baseData = dataBase.DataManager()

    #trabalha com a sessão e verifica se esta logado

    if "userID" in session:
        cpf = session['userID']
        dataName = "cpf"

        dataAchou, tupleLogado = baseData.getDataInfo("logado", dataName, session['userID'])

        if dataAchou:
            dataAchou = (tupleLogado[0][1] == session['loginHash'])

            if dataAchou:
                if session['userType'] == 'M':
                    return redirect('/logged')

        if not dataAchou:
            session.pop("loginHash", None)
            session.pop("userName", None)
            session.pop("userID", None)
            session.pop("userType", None)
            return redirect('/login')
    else:
        session.pop("loginHash", None)
        session.pop("userName", None)
        session.pop("userID", None)
        session.pop("userType", None)
        return redirect('/login')

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

