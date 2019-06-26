from sharedData import session
from flask import redirect,Blueprint
logout_api = Blueprint('logout_api', __name__)

@logout_api.route('/logout')
def logout():
    global usersDataOnline
    #userData.logOutUser()
    #usersDataOnline.logoutUser(session['user'])

    #retira do login data

    session.pop("loginHash", None)
    session.pop("userName", None)
    session.pop("userID", None)
    session.pop("userType", None)

    return redirect('/')
