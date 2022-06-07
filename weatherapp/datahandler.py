import requests
import json
from sqlalchemy import exc
from weatherapp import db
from weatherapp.models import  currentcast

class datahandler:
    def __init__(self):
        pass

    # get forecast for locations
    def getforecast(self,lstlocations:list):

        lstdata = []
        params = {"key":"b3261e9f7baf48229b9113158222805"}
        for location in lstlocations:
            params["q"]=location
            # get request for specific woeid
            response = requests.get("https://api.weatherapi.com/v1/current.json",params=params)
            # turn  response into string
            redata= response.text
            data = json.loads(redata)
            print(data)
            lstdata.append(data)
            # create a list of dictionaries per weather report
        return lstdata


    
    # create objects per forecast
    def dataparser(self,citycast:list):
        # list of forecast objects
        lstofcasts = []    
        # iterate over each cities current forecast
        for cast in citycast:
            print(cast["current"]["wind_mph"],cast["current"]["wind_degree"])
            lstofcasts.append(currentcast(cast["location"]["name"],cast["location"]["region"],cast["location"]["country"],cast["location"]["lat"],\
            cast["location"]["lon"],cast["location"]["tz_id"],cast["current"]["last_updated"],cast["current"]["last_updated_epoch"],\
            cast["location"]["localtime"],cast["location"]["localtime_epoch"],cast["current"]["condition"]["text"],cast["current"]["temp_c"],cast["current"]["temp_f"],\
            cast["current"]["feelslike_c"],cast["current"]["feelslike_f"],cast["current"]["wind_kph"],cast["current"]["wind_mph"],\
            cast["current"]["wind_dir"],cast["current"]["wind_degree"],cast["current"]["pressure_in"],\
            cast["current"]["pressure_mb"],cast["current"]["humidity"],cast["current"]["vis_km"],\
            cast["current"]["vis_miles"],cast["current"]["precip_mm"],cast["current"]["pressure_in"],cast["current"]["cloud"],\
            cast["current"]["uv"],cast["current"]["gust_kph"],cast["current"]["gust_mph"],cast["current"]["is_day"]))
        return  lstofcasts  
            





    # insert data into SQL server
    # try without passing db in class
    def insertdata(self,data):

        for forecast in data:
            try:
                db.session.add(forecast)
                db.session.commit()
            except exc.IntegrityError as err:
                print("Integrity error {}".format(err))
                db.session.rollback()









