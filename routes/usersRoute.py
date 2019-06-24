from sharedData import *
from sharedData import usersDataOnline

users_api = Blueprint('users_api', __name__)

# users registers
@users_api.route('/users', methods=['GET'])
def users():
    global usersDataOnline
    cur = connectionData.getConnector().cursor()
    cur.execute("SELECT * FROM paciente")
    userDetails = cur.fetchall()
    print("tipo de cur.fetchall() = "+ str(type(userDetails)))
    return render_template('users.html',userDetails=userDetails)

