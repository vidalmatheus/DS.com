from sharedData import session,dataBase
from flask import redirect,Blueprint
from modules import dataBase
import sharedData
logout_api = Blueprint('logout_api', __name__)

@logout_api.route('/logout')
def logout():
    baseData = dataBase.DataManager()

    if 'userID' in session:

        ###############RETIRA DO LOGADO
        baseData.deleteData("logado", session["loginHash"],"session_hash")
        session.pop("loginHash", None)
        session.pop("userName", None)
        session.pop("userID", None)
        session.pop("userType", None)

    return redirect('/')
