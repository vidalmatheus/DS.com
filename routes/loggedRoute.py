#from sharedData import *
from flask import Flask, render_template, request, redirect,Blueprint, json, url_for, session

logged_api = Blueprint('logged_api', __name__)


# logged page
@logged_api.route('/logged', methods=['GET'])
def logged():

    if not ("userCPF" in session):
        return redirect('/login')
    print(request.args.get('userDetails'))
    #userData = usersDataOnline.getUser(session['user'])
    if not "verifica no banco de dados se esta logado" == "verifica no banco de dados se esta logado":

        session.pop("loginHash", None)
        session.pop("userName", None)
        session.pop("userCPF", None)
        session.pop("userType", None)

        return redirect('/login')

    return render_template('logged.html',userDetails = userData.getName())

