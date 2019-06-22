from sharedData import *

users_api = Blueprint('users_api', __name__)

# users registers
@users_api.route('/users')
def users():
    cur = con.cursor()
    cur.execute("SELECT * FROM paciente")
    userDetails = cur.fetchall()
    return render_template('users.html',userDetails=userDetails)

