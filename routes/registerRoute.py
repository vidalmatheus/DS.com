from sharedData import *

register_api = Blueprint('register_api', __name__)

# register
@register_api.route('/register', methods=['GET', 'POST'])
def register():
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
        cur = getData().cursor()
        print(cpf,psd,saram,name,birth_date,sex,adress,phone,email,military)
        hashed = bcrypt.hashpw(psd.encode(),bcrypt.gensalt(12))
        hashedDecoded = hashed.decode('utf-8')
        print(hashed)
        print("decoded hash = " + hashedDecoded)
        print("tamanho = " + str(len(hashedDecoded)))
        cur.execute("INSERT INTO paciente VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(cpf,hashedDecoded,saram,name,birth_date,sex,adress,phone,email,military,False))
        #commit the transcation
        getData().commit()
        #close the cursor
        cur.close()
        return redirect('/users')
    return render_template('register.html')

