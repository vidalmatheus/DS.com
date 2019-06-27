from sharedData import session
from flask import render_template, request, redirect,Blueprint
from modules import dataBase
import bcrypt, datetime
import sharedData

register_api = Blueprint('register_api', __name__)
 

# register
@register_api.route('/register', methods=['GET', 'POST'])
def register():
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
                    return redirect('/logged')

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
        print("/////////////////////////")
        print("Comeca route register")
        # Fetch form data
        userDetails = request.form
        cpf = userDetails['cpf']
        psd = userDetails['psd']
        saram = userDetails['saram']
        name = userDetails['name']
        birth_date = userDetails['birth_date']
        sex = userDetails['sex']
        adress = userDetails['adress']
        phone = userDetails['phone']
        email = userDetails['email']
        military = userDetails['military']
        #cursor
        #cur = connectionData.getConnector().cursor()
        #print(cpf +" "+ psd +" "+ saram +" "+ name +" "+ birth_date +" "+ sex +" "+ adress +" "+ phone +" "+ email +" "+ military)

        hashed = bcrypt.hashpw(psd.encode(),bcrypt.gensalt(12))
        hashedDecoded = hashed.decode('utf-8')

        #VERIFICA SE SARAM/CPF É VALIDO

        achouInvalidante ,tupleLook = baseData.getDataInfo("paciente","saram",saram)
        if not achouInvalidante:
            achouInvalidante ,tupleLook = baseData.getDataInfo("paciente","cpf", cpf)
            if achouInvalidante:
                print("CPF " + cpf + " JA CADASTRADO")
                return redirect("/register")
        else:
            print("SARAM " + saram + " JA CADASTRADO" )

        if achouInvalidante:
            return redirect("/register")

        #SE NAO É VALIDO RETORNA PARA O REGISTER

        #ADCIONA O PACIENTE
        tupleData = baseData.addDataThenGetIt("paciente", (cpf,hashedDecoded,saram,name,birth_date,sex,adress,phone,email,military,False))
        #commit the transcation

        userData.setUser(tupleData)
        session["loginHash"] = bcrypt.hashpw((userData.getName()+userData.getCPF()+str(datetime.datetime.now())).encode(),bcrypt.gensalt(12)).decode('utf-8')
        ###########loga paciente
        tupleData = baseData.addDataThenGetIt("logado", (cpf, session["loginHash"]))
        session["userName"] = userData.getName()
        print("////////////////////////////////NOME REGISTRADO\n=>"+session["userName"])
        session["userID"] = userData.getCPF()
        session['userType'] = 'P'
        ###########aloca usuario logado no banco de dados
        #usersDataOnline.addUserOn(userData)
        #close the cursor
        return redirect('/logged')
    return render_template('register.html')

