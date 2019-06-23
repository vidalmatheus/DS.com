from sharedData import *
logout_api = Blueprint('logout_api', __name__)

@logout_api.route('/logout')
def logout():
    #userData.logOutUser()
    print("/////////////////////////////")
    print("Começa logout")
    usersDataOnline.logoutUser(session['user'])
    session.pop('user', None)
    print("usersDataOnline.dictUsersOn = " + str(usersDataOnline.dictUsersOn))
    return redirect('/')
