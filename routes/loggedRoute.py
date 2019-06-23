from sharedData import *

logged_api = Blueprint('logged_api', __name__)

# logged page
@logged_api.route('/logged', methods=['GET'])
def logged():
    if not userData.getLogged():
        return redirect('/login')
    print(request.args.get('userDetails'))
    return render_template('logged.html',userDetails = userData.getName())

