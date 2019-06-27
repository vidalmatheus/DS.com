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
    chosen_crm = "--CRM--"
    med = []
    crm = {}
    if request.method == 'GET':
        # Fetch form data
        chosen_esp = request.args.get('esp')
        #chosen_esp = userDetails['esp']
        print(chosen_esp)
        med = baseData.getExecute("SELECT Nome, CRM  FROM medico WHERE especialidade = %s",(chosen_esp,))
        print(med)
    else:
        #------- Caregando o médico -------
        chosen_medic = request.form['medico']
        print(chosen_medic)
        chosen_crm = baseData.getExecute("SELECT CRM  FROM medico WHERE nome = %s",(chosen_medic,))[0][0]
        baseData.getExecute()
        print(chosen_crm)
        #------- Caregando a descrição do pedido de consulta -------
        desc = request.form['desc']
        print(desc)
    
    cur = baseData.getConnector()
    #------- Caregando as consultas marcadas -------
    cur.execute("select p.Nome as Paciente, k.Nome as Medico, dia, hora_inicio, hora_fim from (medico as m inner join consulta as c on (m.CRM=c.CRM) ) as k inner join paciente as p on (k.CPF_pac=p.CPF)")
    tabela = cur.fetchall()
    # tamanho 
    cur.execute("select count(id) from consulta")
    n = cur.fetchall()[0][0]

    cur.execute("select hora_inicio, hora_fim from consulta where dia = 'Segunda'")
    aux = cur.fetchall()
    segunda = [[],[]]
    print(aux[0][0])
    print(aux[0][1])
    nAux = len(aux)
    i = 0
    segunda_ini=[]
    segunda_fim=[]
    while i<nAux:
        segunda_ini.append(aux[i][0])
        segunda_fim.append(aux[i][1])
        i = i+1
    '''for fim in aux[1]:
        segunda[1].append(fim)
        segunda[1].append(fim)'''
    print(segunda)

    cur.execute("select hora_inicio, hora_fim from consulta where dia = 'Terça'")
    terca = cur.fetchall()

    cur.execute("select hora_inicio, hora_fim from consulta where dia = 'Quarta'")
    quarta = cur.fetchall()

    cur.execute("select hora_inicio, hora_fim from consulta where dia = 'Quinta'")
    quinta = cur.fetchall()

    cur.execute("select hora_inicio, hora_fim from consulta where dia  = 'Sexta'")
    sexta = cur.fetchall()




    return render_template('logged.html',  userDetails=session['userName'],especialidades=especs,chosen_esp=chosen_esp,medicos=med,chosen_medic=chosen_medic,tabela=tabela,n=n,segunda_ini=segunda_ini,segunda_fim=segunda_fim,terca=terca,quarta=quarta,quinta=quinta,sexta=sexta)

