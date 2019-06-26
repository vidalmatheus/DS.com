#from sharedData import *
from flask import redirect,Blueprint, session
logout_api = Blueprint('logout_api', __name__)

@logout_api.route('/logout')
def logout():
    #userData.logOutUser()
    #usersDataOnline.logoutUser(session['user'])

    #retira do login data

    session.pop("loginHash", None)
    session.pop("userName", None)
    session.pop("userCPF", None)
    session.pop("userType", None)

    return redirect('/')
