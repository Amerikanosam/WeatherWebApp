from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import urllib


app = Flask(__name__)
print("The name of the app is {}".format(__name__))
# set database location in flask config file
params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=MARCOS-PC;DATABASE=ForecastDB;Trusted_Connection=yes')
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc:///?odbc_connect=%s"%params
# adds overhead
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#create database instance
db = SQLAlchemy(app)

from weatherapp import routes 