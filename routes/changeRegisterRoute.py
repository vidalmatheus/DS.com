from sharedData import *

changeRegister_api = Blueprint('changeRegister_api', __name__)

# users registers
@changeRegister_api.route('/changeregister')
def changeRegister():
    return render_template('changeRegister.html')
