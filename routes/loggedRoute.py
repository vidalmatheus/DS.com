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
    if not usersDataOnline.userIsOn(session['user']):
        print("user has cookie but not logged, redirect to login")
        session.pop('user', None)
        return redirect('/login')
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
    med=[]
    if request.method == 'GET':
        # Fetch form data
        chosen_esp = request.args.get('esp')
        #chosen_esp = userDetails['esp']
        print(chosen_esp)
        cur.execute("SELECT Nome, CRM  FROM medico WHERE especialidade = %s",(chosen_esp,))
        med = cur.fetchall()
        print(med)
    else:
        #------- Caregando a descrição do pedido de consulta -------
        chosen_medic = request.form['medico']
        desc = request.form['desc']
        print(chosen_medic)
        print(desc)
        




    return render_template('logged.html', userDetails=userData.getName(),especialidades=especs,chosen_esp=chosen_esp,medicos=med,chosen_medic=chosen_medic)
