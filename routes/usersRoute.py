#from sharedData import *
from flask import render_template,Blueprint
from modules import dataBase
users_api = Blueprint('users_api', __name__)

# users registers
@users_api.route('/users', methods=['GET'])
def users():
    baseData = dataBase.DataManager()
    userDetails = baseData.getAllInfoDataType('paciente')
    print("tipo de userDetails = "+ str(type(userDetails)))
    return render_template('users.html',userDetails=userDetails)

