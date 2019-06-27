from sharedData import session, dataBase
from flask import Flask, render_template, request, redirect,Blueprint, json, url_for
from modules import dataBase
import sharedData
import time

logged_api = Blueprint('logged_api', __name__)


# logged page
@logged_api.route('/logged', methods=['GET','POST'])
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

    # ------- Caregando as informações das especialidades dos médicos -------
    especs = baseData.getExecute("SELECT distinct especialidade FROM medico ORDER BY especialidade")
    i = 0
    key_esp={}
    for e in especs:
        key_esp[e[0]] = i # chaves de cada especialidade
        i = i+1
    for e in especs:
        print(e[0])
    # ------- Caregando os médicos de cada especialidade -------
    print ("---------------------")
    chosen_esp = "--Escolha a Especialidade--"
    chosen_medic = "--Escolha um Médico--"
    med=[]
    if request.method == 'GET':
        # Fetch form data
        chosen_esp = request.args.get('esp')
        #chosen_esp = userDetails['esp']
        print(chosen_esp)
        med = baseData.getExecute("SELECT Nome, CRM  FROM medico WHERE especialidade = %s",(chosen_esp,))
        print(med)
    else:
        #------- Caregando a descrição do pedido de consulta -------
        chosen_medic = request.form['medico']
        desc = request.form['desc']
        print(chosen_medic)
        print(desc)





    return render_template('logged.html', userDetails=session['userName'],especialidades=especs,chosen_esp=chosen_esp,medicos=med,chosen_medic=chosen_medic)
