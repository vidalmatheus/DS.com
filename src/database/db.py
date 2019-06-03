from flask import Flask, render_template, request, redirect
import psycopg2

# create app
db = Flask(__name__)

#connect to the db 
con = psycopg2.connect(
            host = "localhost",
            database="ds",
            user = "postgres",
            password = "admin")

@db.route('/', methods=['GET', 'POST'])
def index():
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
    return render_template('index.html')

@db.route('/users')
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
    db.run(debug=True)
    #close the connection
    con.close()

