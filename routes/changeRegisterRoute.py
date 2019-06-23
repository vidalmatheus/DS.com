from sharedData import *

changeRegister_api = Blueprint('changeRegister_api', __name__)

# users registers
@changeRegister_api.route('/changeregister', methods=['GET', 'POST'])
def changeRegister():
    print("////////////////////////////////////////")
    print("comeca change register")
    print("usersDataOnline.getDictionary() = "+ str(usersDataOnline.getDictionary()))
    userData = usersDataOnline.getUser(session['user'])
    print("usersDataOnline.getDictionary() = "+ str(usersDataOnline.getDictionary()))
    if userData == None:
        print("usersDataOnline.getUser(session['user']) == None")
        if 'user' in session:
            session.pop('user', None)
        return redirect('/logged')
    user_list = userData.getStringList()
    print("userData.getStringList() = "+ str(user_list))
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
            cur = connectionData.getConnector().cursor()
            #print(cpf +" "+ psd +" "+ saram +" "+ name +" "+ birth_date +" "+ sex +" "+ adress +" "+ phone +" "+ email +" "+ military)
            hashed = bcrypt.hashpw(psd.encode(),bcrypt.gensalt(12))
            hashedDecoded = hashed.decode('utf-8')
            cur.execute("SELECT senha FROM paciente WHERE saram = %s",(saram,))
            psd_db = cur.fetchall()
            psd_db = psd_db[0][0]
            if (bcrypt.hashpw(psd.encode(),psd_db.encode()) != psd_db.encode() and len(psd) != 0):      
                cur.execute("UPDATE paciente SET senha=%s,nome=%s,dt_nasc=%s,sexo=%s,endereco=%s,telefone=%s,email=%s,militar=%s WHERE saram=%s",(hashedDecoded,name,birth_date,sex,adress,phone,email,military,saram))
            else:
                cur.execute("UPDATE paciente SET nome=%s,dt_nasc=%s,sexo=%s,endereco=%s,telefone=%s,email=%s,militar=%s WHERE saram=%s",(name,birth_date,sex,adress,phone,email,military,saram)) 
            #commit the transcation
            connectionData.getConnector().commit()
            cur.execute("SELECT * FROM paciente WHERE saram = %s",(saram,))

            #apaga no dictionary a usuario
            cpf = session['user']
            usersDataOnline.logoutUser(cpf)
            userData = usuario.acessoUser()

            user = cur.fetchall()
            userData.logginUser(user[0])
            usersDataOnline.addUserOn(userData)

            print("ATUALIZAÇÃO DOS DADOS COM SUCESSO")
            #close the cursor
            cur.close()
            return redirect('/logged')
        elif (submit == "Cancelar"): return redirect('/logged')
    return render_template('changeRegister.html',userDetails = user_list)

