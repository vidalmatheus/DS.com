from flask import Flask, render_template, request, redirect, json, url_for
import psycopg2

# create app
app = Flask(__name__,static_url_path='/static')

### connect to the db 
con = psycopg2.connect(
            host = "ec2-50-19-114-27.compute-1.amazonaws.com",
            database="d4hj7938me3577",
            user = "pjiswamglyhfme",
            port = 5432,
            password = "2829cb6cc89be5cfbe36da3706dfe468c9b8a46c2f2560f85ac05e5ec7870b80")
####

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        cpf = userDetails['cpf']
        senha = userDetails['senha']
        saram = userDetails['saram']
        nome = userDetails['nome']
        dt_nasc = userDetails['dt_nasc']
        sexo = userDetails['sexo']
        endereco = userDetails['endereco']
        tel = userDetails['telefone']
        email = userDetails['email']
        militar = userDetails['militar']
        #cursor 
        cur = con.cursor()  
        print(cpf,senha,saram,nome,dt_nasc,sexo,endereco,tel,email,militar)
        cur.execute("INSERT INTO paciente VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(cpf,senha,saram,nome,dt_nasc,sexo,endereco,tel,email,militar,False))
        #commit the transcation 
        con.commit()
        #close the cursor
        cur.close()
        return redirect('/users')
    return render_template('cadastro.html')

@app.route('/users')
def users():
    cur = con.cursor()  
    resultValue = cur.execute("SELECT * FROM paciente")
    userDetails = cur.fetchall()
    return render_template('users.html',userDetails=userDetails)

'''
#--- incio: teste externo
cur.execute("select CPF, nome from paciente")
rows = cur.fetchall()

print ("CPF             Nome")
for r in rows:
    print (f" {r[0]} | {r[1]} ")

#--- fim: teste externo
'''

if __name__ == '__main__':
    app.run(debug=True)
    #close the connection
    con.close()

