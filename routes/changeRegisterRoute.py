from sharedData import *

changeRegister_api = Blueprint('changeRegister_api', __name__)

# users registers
@changeRegister_api.route('/changeregister', methods=['GET', 'POST'])
def changeRegister():
    userDetails = userData.getStringList()
    #userDetails = userData.getName()
    print("tipo de userData.getStringList() = " + str(type(userDetails)))
    print("tipo de userData.getStringList()[0] = " + str(type(userDetails[0])))
    print("tipo de string = " + str(type("01455sdsa")))
    print("userData.getStringList()[0] = " + userDetails[0])
    return render_template('changeRegister.html',userDetails = userDetails)

