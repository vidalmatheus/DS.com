from flask import Flask, render_template, request, redirect, json, url_for
import psycopg2, subprocess
from config import *

# create app
app = Flask(__name__,static_url_path='/static')

# main page
@app.route('/')
def index():
    return render_template('index.html')

# login page
@app.route('/login')
def login():
    return render_template('login.html')

# 
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

