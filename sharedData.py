from flask import Flask, render_template, request, redirect,Blueprint, json, url_for, session
from modules import dataBase,usuario
import psycopg2, os, subprocess, bcrypt

#
#def getData():
#    DATABASE_URL = os.environ['DATABASE_URL']
#    con = psycopg2.connect(DATABASE_URL, sslmode='require')
#    return con



### connect to the dataBase
DATABASE_URL = os.environ['DATABASE_URL']
connectionData = dataBase.dataAccess()
####

###Usuario
usersDataOnline = usuario.acessManager()
#userData = usuario.acessoUser()
###



