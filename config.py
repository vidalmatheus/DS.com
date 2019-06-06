import psycopg2
import subprocess

### connect to the db 
proc = subprocess.Popen('heroku config:get DATABASE_URL -a divisaosaude', stdout=subprocess.PIPE, shell=True)
db_url = proc.stdout.read().decode('utf-8').strip() + '?sslmode=require'
con = psycopg2.connect(db_url)
####
