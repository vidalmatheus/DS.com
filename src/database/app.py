from flask import Flask
import sqlalchemy as db
from sqlalchemy import *

app = Flask(__name__)

# connect to the db
engine = create_engine('postgresql://postgres:admin@localhost/ds')
con = engine.connect()

@app.route("/hello")
def hello():
    return "<h1>Hello BRAZIL! !!!!!!</h1>"

@app.route("/hello/<name>")
def get_name(name):
    return "<h1>Hello, {}!</h1>".format(name)

sql = text('SELECT * FROM paciente')
ans = con.execute(sql)
names = [row[3] for row in ans]
print(names)

@app.route("/paciente")
def get_paciente():
    return f"{names}"

con.close()

if __name__ == '__main__':
    app.run(debug=True)


