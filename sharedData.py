from flask import Flask, render_template, request, redirect,Blueprint, json, url_for
import psycopg2, os, subprocess, bcrypt
from routes import loginRoute,registerRoute,loggedRoute,usersRoute,changeRegisterRoute

### connect to the dataBase
DATABASE_URL = os.environ['DATABASE_URL']
con = psycopg2.connect(DATABASE_URL, sslmode='require')
####