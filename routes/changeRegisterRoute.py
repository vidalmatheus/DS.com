from sharedData import *

changeRegister_api = Blueprint('changeRegister_api', __name__)

# users registers
@changeRegister_api.route('/changeregister', methods=['GET', 'POST'])
def changeRegister():
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
        #print(cpf +" "+ psd +" "+ saram +" "+ name +" "+ birth_date +" "+ sex +" "+ adress +" "+ phone +" "+ email +" "+ military)
        hashed = bcrypt.hashpw(psd.encode(),bcrypt.gensalt(12))
        hashedDecoded = hashed.decode('utf-8')
        cur.execute("INSERT INTO paciente VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(cpf,hashedDecoded,saram,name,birth_date,sex,adress,phone,email,military,False))
        #commit the transcation
        connectionData.getConnector().commit()
        #close the cursor
        cur.close()
        return redirect('/logged')
    return render_template('register.html')

    userData = usersDataOnline.getUser(session['user'])
    userDetails = userData.getStringList()
    #userDetails = userData.getName()
    print("tipo de userData.getStringList() = " + str(type(userDetails)))
    print("tipo de userData.getStringList()[0] = " + str(type(userDetails[0])))
    print("tipo de string = " + str(type("01455sdsa")))
    print("userData.getStringList()[0] = " + userDetails[0])
    return render_template('changeRegister.html',userDetails = userDetails)

