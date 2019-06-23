from sharedData import *
logout_api = Blueprint('logout_api', __name__)

@logout_api.route('/logout')
def logout():
    userData.logOutUser()
    return redirect('/')