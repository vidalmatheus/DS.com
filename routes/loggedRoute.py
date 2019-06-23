from sharedData import *

logged_api = Blueprint('logged_api', __name__)


# logged page
@logged_api.route('/logged', methods=['GET'])
def logged():
    print('/////////////////////////')
    print("logged_api.route")
    if not ('user' in session):
        printf("user not in session, redirect to login")
        return redirect('/login')
    print(request.args.get('userDetails'))
    userData = usersDataOnline.getUser(session['user'])
    if not usersDataOnline.userIsOn(session['user']):
        printf("user has cookie but not logged, redirect to login")
        session.pop('user', None)
        return redirect('/login')
    printf("render logged")
    return render_template('logged.html',userDetails = userData.getName())

