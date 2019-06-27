from sharedData import session
from flask import render_template, request, redirect,Blueprint
from modules import dataBase
import bcrypt, datetime

register_api = Blueprint('register_api', __name__)

# register
@register_api.route('/register', methods=['GET', 'POST'])
def register():
    userData = dataBase.PessoaUserData()
    baseData = dataBase.DataManager()


    if "userCPF" in session:
        if "verifica se esta loggado com o 'loginHash' correto"== "verifica se esta loggado com o 'loginHash' correto":
            # session["loginHash"]
            # session["userName"] = userData.getName()
            # session["userCPF"]
            return redirect('/logged')
        else:
            session.pop("loginHash", None)
            session.pop("userName", None)
            session.pop("userID", None)
            session.pop("userType", None)

            return redirect('/register')

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
        session["userName"] = userData.getName()
        print("////////////////////////////////NOME REGISTRADO\n=>"+session["userName"])
        session["userID"] = userData.getCPF()
        session['userType'] = 'P'
        ###########aloca usuario logado no banco de dados
        #usersDataOnline.addUserOn(userData)
        #close the cursor
        return redirect('/logged')
    return render_template('register.html')

