from sharedData import *

logged_api = Blueprint('logged_api', __name__)


# logged page
@logged_api.route('/logged', methods=['GET'])
def logged():
    if not ('user' in session):
        return redirect('/login')
    print(request.args.get('userDetails'))
    userData = usersDataOnline.getUser(session['user'])
    return render_template('logged.html',userDetails = userData.getName())

