from sharedData import *
from collections import namedtuple

logged_api = Blueprint('logged_api', __name__)


# logged page
@logged_api.route('/logged', methods=['GET','POST'])
def logged():
    global usersDataOnline
    print('/////////////////////////')
    print("Comeca logged")
    print("usersDataOnline.dictUsersOn = "+str(usersDataOnline.dictUsersOn))
    if not ('user' in session):
        print("user not in session, redirect to login")
        return redirect('/login')
    print(request.args.get('userDetails'))
    userData = usersDataOnline.getUser(session['user'])
    #if not usersDataOnline.userIsOn(session['user']):
    #    print("user has cookie but not logged, redirect to login")
    #    session.pop('user', None)
    #    return redirect('/login')
    print("render logged")
    
    # cursor
    cur = connectionData.getConnector().cursor()
    # ------- Caregando as informações das especialidades dos médicos -------
    cur.execute("SELECT distinct especialidade FROM medico ORDER BY especialidade")
    especs = cur.fetchall()
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
        if (chosen_esp == None): chosen_esp = "--Escolha a Especialidade--"
        print(chosen_esp)
        cur.execute("SELECT Nome, CRM  FROM medico WHERE especialidade = %s",(chosen_esp,))
        med = cur.fetchall()
    else:
        #------- Caregando o médico -------
        chosen_medic = request.form['medico']
        print(chosen_medic)
        cur.execute("SELECT CRM  FROM medico WHERE nome = %s",(chosen_medic,))
        chosen_crm = cur.fetchall()[0][0]
        print(chosen_crm)
        #------- Caregando a descrição do pedido de consulta -------
        desc = request.form['desc']
        print(desc)

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








    return render_template('logged.html', userDetails=userData.getName(),especialidades=especs,chosen_esp=chosen_esp,medicos=med,chosen_medic=chosen_medic,tabela=tabela,n=n,segunda_ini=segunda_ini,segunda_fim=segunda_fim,terca=terca,quarta=quarta,quinta=quinta,sexta=sexta)
