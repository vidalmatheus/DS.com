from sharedData import *

register_api = Blueprint('register_api', __name__)
 

# register
@register_api.route('/register', methods=['GET', 'POST'])
def register():
    global usersDataOnline
    alert = ""
    if request.method == 'POST':
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
        cur = connectionData.getConnector().cursor()
        # verifica se saram já existe:
        print(saram)
        if (len(saram)>0): 
            print("Colocou SARAM")
            cur.execute("SELECT saram FROM paciente WHERE saram = %s",(saram,))
            if (len(cur.fetchall())>0): # saram já existe
                alert = "SARAM já existente. Efetuar login."
        if (alert == ""):
            saram = None
            cur.execute("SELECT cpf FROM paciente WHERE cpf = %s",(cpf,))  
            if (len(cur.fetchall())>0): # cpf já existe
                alert = "CPF já existente. Efetuar login."
            else:
                #print(cpf +" "+ psd +" "+ saram +" "+ name +" "+ birth_date +" "+ sex +" "+ adress +" "+ phone +" "+ email +" "+ military)
                hashed = bcrypt.hashpw(psd.encode(),bcrypt.gensalt(12))
                hashedDecoded = hashed.decode('utf-8')
                cur.execute("INSERT INTO paciente VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(cpf,hashedDecoded,saram,name,birth_date,sex,adress,phone,email,military,False))
                #commit the transcation
                connectionData.getConnector().commit()
                userData = usuario.acessoUser()
                cur.execute("SELECT * FROM paciente WHERE cpf = %s",(cpf,))
                user = cur.fetchall()
                print("adciona user[0] = " + str(user[0]))
                userData.logginUser(user[0])
                print("userData.getStringList() = " + str(userData.getStringList()))
                session['user'] = cpf
                usersDataOnline.addUserOn(userData)
                print("after added user on login")
                print("session['user'] = "+ session['user'])
                print("usersDataOnline.getDictionary() = "+ str(usersDataOnline.getDictionary()))
                #close the cursor
                cur.close()
                return redirect('/logged')
    return render_template('register.html',alert=alert)

