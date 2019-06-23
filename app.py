from sharedData import *
from routes import loginRoute,logoutRoute,registerRoute,loggedRoute,usersRoute,changeRegisterRoute

# create app
app = Flask(__name__,static_url_path='/static')

#blueprint
app.register_blueprint(loginRoute.login_api)
app.register_blueprint(logoutRoute.logout_api)
app.register_blueprint(registerRoute.register_api)
app.register_blueprint(loggedRoute.logged_api)
app.register_blueprint(usersRoute.users_api)
app.register_blueprint(changeRegisterRoute.changeRegister_api)
# main page
@app.route('/')
def index():
    if userData.getLogged():
        return redirect('/logged')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,threaded=True)
    #close the connection
    connectionData.getConnector().close()

