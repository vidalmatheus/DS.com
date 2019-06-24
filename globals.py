from modules.usuario import usuario

def initialize():
    global usersDataOnline
    usersDataOnline = usuario.acessManager()