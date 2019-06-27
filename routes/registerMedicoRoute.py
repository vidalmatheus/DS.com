from sharedData import session
from flask import render_template, request, redirect,Blueprint
from modules import dataBase
import bcrypt, datetime

medicoRegister_api = Blueprint('medicoRegister_api', __name__)


# register
@medicoRegister_api.route('/registerMedico', methods=['GET', 'POST'])
def register():
    print("/////////////////////////")
    print("Comeca Medicoroute register")
    medicoData = dataBase.MedicoUserData()
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

            return redirect('/registerMedico')

    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        cpf = userDetails['cpf']
        psd = userDetails['psd']
        saram = userDetails['saram']
        name = userDetails['name']
        military = userDetails['military']
        especialidade = userDetails['especialidade']
        crm = userDetails["crm"]
        #cursor
        #cur = connectionData.getConnector().cursor()
        #print(cpf +" "+ psd +" "+ saram +" "+ name +" "+ birth_date +" "+ sex +" "+ adress +" "+ phone +" "+ email +" "+ military)

        hashed = bcrypt.hashpw(psd.encode(),bcrypt.gensalt(12))
        hashedDecoded = hashed.decode('utf-8')

        # VERIFICA SE SARAM/CPF É VALIDO

        achouInvalidante, tupleLook = baseData.getDataInfo("medico", "saram", saram)
        if not achouInvalidante:
            achouInvalidante, tupleLook = baseData.getDataInfo("medico", "cpf", cpf)
            if achouInvalidante:
                print("CPF " + cpf + " JA CADASTRADO")
                return redirect("/registerMedico")
            else:
                achouInvalidante, tupleLook = baseData.getDataInfo("medico", "crm", crm)
                if achouInvalidante:
                    print("CRM " + crm + " JA CADASTRADO")

        else:
            print("SARAM " + saram + " JA CADASTRADO")

        if achouInvalidante:
            return redirect("/registerMedico")

        # SE NAO É VALIDO RETORNA PARA O REGISTER

        tupleData = baseData.addDataThenGetIt("Medico", (cpf,hashedDecoded,saram,name,military, crm, especialidade))
        #commit the transcation

        medicoData.setUser(tupleData)
        session["loginHash"] = bcrypt.hashpw((medicoData.getName()+medicoData.getCPF()+str(datetime.datetime.now())).encode(),bcrypt.gensalt(12)).decode('utf-8')
        session["userName"] = medicoData.getName()
        print("////////////////////////////////NOME REGISTRADO\n=>"+session["userName"])
        session["userID"] = medicoData.getCPF()
        session['userType'] = 'M'
        ###########aloca usuario logado no banco de dados
        #usersDataOnline.addUserOn(userData)
        #close the cursor
        return redirect('/logged')
    return render_template('registerMedico.html')

