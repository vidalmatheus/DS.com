from sharedData import *

logged_api = Blueprint('logged_api', __name__)

# logged page
@logged_api.route('/logged')
def logged():
    print(request.args.get('userDetails'))
    return render_template('logged.html',userDetails=request.args.get('userDetails'))

