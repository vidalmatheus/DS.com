from sharedData import session, dataBase
from flask import Flask, render_template, redirect
from routes import loginRoute,logoutRoute,registerRoute,loggedRoute,usersRoute,changeRegisterRoute, registerMedicoRoute
from routes import medicosRoute
import logging, sys
import sharedData
import time

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
app.register_blueprint(registerMedicoRoute.medicoRegister_api)
app.register_blueprint(medicosRoute.medicos_api)

# main page
@app.route('/')
def index():
    start = time.time()
    baseData = dataBase.DataManager()
    loginType = ""
    # verifica se session is correct

    # trabalha com a sessão e verifica se esta logado

    if "userID" in session:
        cpf = session['userID']
        dataName = "cpf"

        dataAchou, tupleLogado = baseData.getDataInfo("logado", dataName, session['userID'])

        if dataAchou:
            dataAchou = (tupleLogado[0][1] == session['loginHash'])

            if dataAchou:
                if session['userType'] == 'P':
                    return redirect('/logged')
                elif session['userType'] == 'M':
                    return redirect('/logged')

        if not dataAchou:
            session.pop("loginHash", None)
            session.pop("userName", None)
            session.pop("userID", None)
            session.pop("userType", None)
    else:
        session.pop("loginHash", None)
        session.pop("userName", None)
        session.pop("userID", None)
        session.pop("userType", None)

    # caso esteja apropridamente logado continua

    end = time.time()
    print("FLAG05 " + str(end - start))
    return render_template('index.html')


if __name__ == '__main__':
    print('tipo de session = '+str(type(session)))
    app.run(debug=True,threaded=True)
    #close the connection

