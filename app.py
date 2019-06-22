from flask import Flask, render_template, request, redirect, json, url_for
import psycopg2, os, subprocess, bcrypt

# create app
app = Flask(__name__,static_url_path='/static')

### connect to the db 
DATABASE_URL = os.environ['DATABASE_URL']
con = psycopg2.connect(DATABASE_URL, sslmode='require')
####

# main page
@app.route('/')
def index():
    return render_template('index.html')

# login page
@app.route('/login', methods=['GET','POST']) ## FALTA FAZER FUNCIONAR ##
def login():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        psd = userDetails['password']
        #cursor 
        cur = con.cursor()  
        errorSARAM = errorCPF = False 
        if (len(userDetails['login']) == 7 or len(userDetails['login']) == 11):
            if (len(userDetails['login']) == 7): 
                saram = userDetails['login']
                cur.execute("SELECT * FROM paciente WHERE saram = %s",(saram,))
                user = cur.fetchall()
                if (len(user)==0): errorSARAM = True 
            elif (len(userDetails['login']) == 11): 
                cpf = userDetails['login']
                #134.202.967-46
                cpf = cpf[0:3]+"."+cpf[3:6]+"."+cpf[6:9]+"-"+cpf[9:11]
                print(cpf)
                cur.execute("SELECT * FROM paciente WHERE cpf = %s",(cpf,))
                user = cur.fetchall()
                if (len(user)==0): errorCPF = True 

            if (errorSARAM): print("SARAM NÃO ENCONTRADO")
            elif (errorCPF): print("CPF NÃO ENCONTRADO")
            else:
                psd_db = user[0][1]
                print(bcrypt.hashpw(psd.encode(),psd_db.encode())) 
                print(psd_db.encode())
                if (bcrypt.hashpw(psd.encode(),psd_db.encode()) == psd_db.encode()): 
                    #close the cursor
                    cur.close()
                    return redirect(url_for('logged',userDetails=user[0][3])) ### FALTA PASSAR ALGUM PARÂMETRO PARA SABER O NOME ###
                else: print("SENHA ERRADA!") ## FALTA JOGAR PRO html
        else: print("ERRO! CPF OU SENHA EM FORMATO INCORRETO!") ## FALTA JOGAR PRO html

    return render_template('login.html')

# register 
@app.route('/register', methods=['GET', 'POST'])
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
        cur = con.cursor()  
        print(cpf,psd,saram,name,birth_date,sex,adress,phone,email,military)
        hashed = bcrypt.hashpw(psd.encode(),bcrypt.gensalt(12))
        hashedDecoded = hashed.decode('utf-8')
        print(hashed)
        print("decoded hash = " + hashedDecoded)
        print("tamanho = " + str(len(hashedDecoded)))
        cur.execute("INSERT INTO paciente VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(cpf,hashedDecoded,saram,name,birth_date,sex,adress,phone,email,military,False))
        #commit the transcation 
        con.commit()
        #close the cursor
        cur.close()
        return redirect('/users')
    return render_template('register.html')

# change register 
@app.route('/changeregister')
def changeRegister():
    return render_template('changeRegister.html')


# logged page
@app.route('/logged')
def logged():
    print(request.args.get('userDetails'))
    return render_template('logged.html',userDetails=request.args.get('userDetails'))

# users registers
@app.route('/users')
def users():
    cur = con.cursor()  
    cur.execute("SELECT * FROM paciente")
    userDetails = cur.fetchall()
    return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)
    #close the connection
    con.close()

