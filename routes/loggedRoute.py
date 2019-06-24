from sharedData import *
import globals
logged_api = Blueprint('logged_api', __name__)


# logged page
@logged_api.route('/logged', methods=['GET'])
def logged():
    global usersDataOnline
    print('/////////////////////////')
    print("Comeca logged")
    print("globals.usersDataOnline.dictUsersOn = "+str(globals.usersDataOnline.dictUsersOn))
    if not ('user' in session):
        print("user not in session, redirect to login")
        return redirect('/login')
    print(request.args.get('userDetails'))
    userData = globals.usersDataOnline.getUser(session['user'])
    if not globals.usersDataOnline.userIsOn(session['user']):
        print("user has cookie but not logged, redirect to login")
        session.pop('user', None)
        return redirect('/login')
    print("render logged")
    return render_template('logged.html',userDetails = userData.getName())

