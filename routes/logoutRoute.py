from sharedData import session
from flask import redirect,Blueprint
from modules import dataBase
logout_api = Blueprint('logout_api', __name__)

@logout_api.route('/logout')
def logout():
    baseData = dataBase.DataManager()

    if 'userID' in session:

        ###############RETIRA DO LOGADO
        baseData.deleteLookVar("logado", "session_hash", session["session_hash"])
        session.pop("loginHash", None)
        session.pop("userName", None)
        session.pop("userID", None)
        session.pop("userType", None)

    return redirect('/')
