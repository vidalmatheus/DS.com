from sharedData import session
from flask import Flask, render_template, request, redirect,Blueprint, json, url_for

logged_api = Blueprint('logged_api', __name__)


# logged page
@logged_api.route('/logged', methods=['GET'])
def logged():
    print("/////////////////////////////\nCOMECA LOGGED")
    if not ("userID" in session):
        print("USER IS NOT IN SESSION")
        return redirect('/login')
    print(request.args.get('userDetails'))
    #userData = usersDataOnline.getUser(session['user'])
    if not "verifica no banco de dados se esta logado" == "verifica no banco de dados se esta logado":
        print("SE TIVER EM SESSION MAS NAO ESTA NO BANCO DE LOGADOS")


        session.pop("loginHash", None)
        session.pop("userName", None)
        session.pop("userCPF", None)
        session.pop("userType", None)

        return redirect('/login')

    print("RENDERIZA A TELA DE LOGGED")
    return render_template('logged.html', userDetails = session['userName'])

