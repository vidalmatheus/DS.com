from sharedData import *
logout_api = Blueprint('logout_api', __name__)

@logout_api.route('/logout')
def logout():
    #userData.logOutUser()
    usersDataOnline.logoutUser(session['user'])
    session.pop('user', None)
    return redirect('/')
