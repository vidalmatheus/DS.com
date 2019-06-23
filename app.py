from sharedData import *

# create app
app = Flask(__name__,static_url_path='/static')

#blueprint
app.register_blueprint(loginRoute.login_api)
app.register_blueprint(registerRoute.register_api)
app.register_blueprint(loggedRoute.logged_api)
app.register_blueprint(usersRoute.users_api)
app.register_blueprint(changeRegisterRoute.changeRegister_api)
# main page
@app.route('/')
def index():
    userData.logOutUser()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    #close the connection
    connectionData.getConnector().close()

