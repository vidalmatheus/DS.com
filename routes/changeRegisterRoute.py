#from sharedData import *
from flask import render_template, request, redirect,Blueprint, session
import bcrypt, datetime
from modules import dataBase

changeRegister_api = Blueprint('changeRegister_api', __name__)

# users registers
@changeRegister_api.route('/changeregister', methods=['GET', 'POST'])
def changeRegister():
    baseData = dataBase.DataManager()
    if "userCPF" in session:
        if "verifica se esta loggado com o 'loginHash' correto"=="verifica se esta loggado com o 'loginHash' correto":
            print('session["loginHash"]' + session["loginHash"])
            #session["userName"] = userData.getName()
            #session["userCPF"]
        else:
            session.pop("loginHash", None)
            session.pop("userName", None)
            session.pop("userCPF", None)
            session.pop("userType", None)

            return redirect('/login')

    userData = dataBase.PessoaUserData()
    userExist,tuplaDataInfo = baseData.getDataInfo("paciente","cpf",session["userCPF"])

    userData.setUser(tuplaDataInfo)

    user_list = userData.getStringList()
    saram = user_list[1]
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        submit = userDetails['submit']
        if (submit == "Enviar" ):
            psd = userDetails['psd']
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
            if len(psd) > 1:
                hashed = bcrypt.hashpw(psd.encode(),bcrypt.gensalt(12))
                hashedDecoded = hashed.decode('utf-8')
                user = baseData.changeDataAndReturnNewData("paciente",
                                                    ["senha", "nome", 'dt_nasc', 'sexo', 'endereco', 'telefone',
                                                     'email', 'militar'],
                                                    [hashedDecoded, name, birth_date, sex, adress, phone, email,
                                                     military], saram, 'saram')
            else:
                user = baseData.changeDataAndReturnNewData("paciente", ["nome", 'dt_nasc', 'sexo', 'endereco', 'telefone',
                                                                 'email', 'militar'],[name,birth_date,sex,adress,phone,email,military],saram,'saram')

            userData = dataBase.PessoaUserData()

            userData.setUser(user)
            session["userName"] = userData.getName()
            print("ATUALIZAÇÃO DOS DADOS COM SUCESSO")

            return redirect('/logged')
        elif (submit == "Cancelar"):
            print("ATUALIZAÇÃO DOS DADOS CANCELADA")
            return redirect('/logged')
    return render_template('changeRegister.html',userDetails = user_list)

