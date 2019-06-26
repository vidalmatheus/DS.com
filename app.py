from sharedData import session
from flask import Flask, render_template, redirect
from routes import loginRoute,logoutRoute,registerRoute,loggedRoute,usersRoute,changeRegisterRoute
import logging, sys

# create app
app = Flask(__name__,static_url_path='/static')
app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

#blueprint
app.register_blueprint(loginRoute.login_api)
app.register_blueprint(logoutRoute.logout_api)
app.register_blueprint(registerRoute.register_api)
app.register_blueprint(loggedRoute.logged_api)
app.register_blueprint(usersRoute.users_api)
app.register_blueprint(changeRegisterRoute.changeRegister_api)
# main page
@app.route('/')
def index():

    if "userCPF" in session:
        if "verifica se esta loggado com o 'loginHash' correto"=="verifica se esta loggado com o 'loginHash' correto":
            #session["loginHash"]
            #session["userName"] = userData.getName()
            #session["userCPF"]
            if session["userType"] == 'P':
               cpf = session['userID']
            elif session["userType"] == 'M':
                crm = session['userID']
            return redirect('/logged')
        else:
            session.pop("loginHash", None)
            session.pop("userName", None)
            session.pop("userID", None)
            session.pop("userType", None)

    return render_template('index.html')

if __name__ == '__main__':
    print('tipo de session = '+str(type(session)))
    app.run(debug=True,threaded=True)
    #close the connection

