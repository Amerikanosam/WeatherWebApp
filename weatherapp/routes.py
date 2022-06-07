from weatherapp import app
from flask import render_template
from weatherapp. models import currentcast
import json


"""@app.route('/')
def getindex():
    return render_template('index.html')
"""

# api for weather forecast per location
@app.route('/api/<location>')
def getlocforecast(location):
    # get forecast for location
    locforecast = forecast.query.filter_by(ForecastLocation=location).limit(5).all()
    # remove the sqalchemy state
    for instance in locforecast:
        instance.__dict__.pop('_sa_instance_state')
    # create a list of dicts
    lstofinstance = [instance.__dict__ for instance in locforecast]
    # dump list of dicts
    return json.dumps(lstofinstance,default=str)

@app.route('/api/today/<location>')
def gettodaysforecast(location):

    dailycast = dailycast.query.filter_by(Location=location).all()
    # remove sql alchemy key
    for instance in dailycast:
         instance.__dict__.pop('_sa_instance_state')

    forecastlst = [ instance.__dict__ for instance in dailycast]

    return json.dumps(forecastlst,default=str)

"""
@app.route('/home')
def student():
    return render_template('student.html')
"""




"""

@app.route('/api/averagetemp/')
def average_temp():

    currenttime = datetime.now()
    num_temp_samples = 3
    avg_temps=[]
    for location in db.session.query(forecasthistory.Location).distinct().all():
        temps = db.session.query(forecasthistory.RealTemp,forecasthistory.CreatedDate ).filter(forecasthistory.Location==location.Location,forecasthistory.CreatedDate<currenttime.strftime('%Y-%m-%d %H:%M:%S')).\
        limit(num_temp_samples).all()
        lsttemp = []
        for row in temps:
            lsttemp.append(row["RealTemp"])
        temperature = Temperatures(location,lsttemp)
        temperature.computeavgtemp()
        avg_temps.append(temperature)
    return render_template('dailyavgtemps.html',dailyavgtemps = avg_temps)

"""
