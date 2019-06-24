from sharedData import *
import globals
logout_api = Blueprint('logout_api', __name__)

@logout_api.route('/logout')
def logout():
    #global usersDataOnline
    #userData.logOutUser()
    print("/////////////////////////////")
    print("Começa logout")
    #if not 'user' in session:
        #print("not 'user' so return to '/'")
        #return redirect('/') 
    globals.usersDataOnline.logoutUser(session['user'])
    session.pop('user', None)
    print("globals.usersDataOnline.dictUsersOn = " + str(globals.usersDataOnline.dictUsersOn))
    return redirect('/')
