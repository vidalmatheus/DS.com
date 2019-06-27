#from sharedData import *
from flask import render_template,Blueprint
from modules import dataBase
medicos_api = Blueprint('medicos_api', __name__)

# users registers
@medicos_api.route('/medicos', methods=['GET'])
def medicos():
    baseData = dataBase.DataManager()
    userDetails = baseData.getAllInfoDataType('Medico')
    print("tipo de userDetails = "+ str(type(userDetails)))
    return render_template('medicosUsers.html',userDetails=userDetails)

