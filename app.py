from flask import Flask, render_template, request, redirect, json, url_for
import psycopg2, os, subprocess,bcrypt

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
        if (len(userDetails['login']) == 7): 
            saram = userDetails['login']
            cur.execute("SELECT senha FROM paciente WHERE saram = %s",(saram,))
        elif (len(userDetails['login']) == 11): 
            cpf = userDetails['login']
            cur.execute("SELECT senha FROM paciente WHERE cpf = %s",(cpf,))
        else: print("ERRO! CONTA NÃO EXISTENTE!") ## FALTA JOGAR PRO html
        psd_db = cur.fetchall()

        print(int.from_bytes(psd_db[0][0], byteorder='big')) ## Tem que converter para inteiro, não sei ##
        if (bcrypt.hashpw(psd.encode(),psd_db[0][0]) == psd_db[0][0]): ## NÃO ESTÁ FUNCIONANDO ##
            #close the cursor
            cur.close()
            return redirect('/logged') ### FALTA PASSAR ALGUM PARÂMETRO PARA SABER O NOME ###

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
        cur.execute("INSERT INTO paciente VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(cpf,psd,saram,name,birth_date,sex,adress,phone,email,military,False))
        #commit the transcation 
        con.commit()
        #close the cursor
        cur.close()
        return redirect('/users')
    return render_template('register.html')

# logged page
@app.route('/logged')
def logged():
    return render_template('logged.html')

# users registers
@app.route('/users')
def users():
    cur = con.cursor()  
    resultValue = cur.execute("SELECT * FROM paciente")
    userDetails = cur.fetchall()
    return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)
    #close the connection
    con.close()

