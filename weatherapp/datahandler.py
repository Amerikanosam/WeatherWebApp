import requests
import json
from sqlalchemy import exc
from weatherapp import db
from weatherapp.models import forecast, dailycast

class datahandler:
    def __init__(self):
        pass


    # get woeids
    def getwoeids(self,locations:list):
        lstwoeids = []
        # get woeid for each location
        for location in locations:
            response = requests.get("https://www.metaweather.com/api/location/search/",params={"query":location})
            data = response.text
            jsdata = json.loads(data)[0]
            #transform response to json object
            lstwoeids.append(jsdata["woeid"])
        return  lstwoeids

    # get forecast for locations
    def getforecast(self,lstlocations:list):

        # get woeids
        woeids = self.getwoeids(lstlocations)

        lstdata = []
        for woeid in woeids:
            # get request for specific woeid
            response = requests.get("https://www.metaweather.com/api/location/{}".format(woeid))
            # turn  response into string
            redata= response.text
            data = json.loads(redata)
            lstdata.append(data)
            # create a list of dictionaries per weather report
        return lstdata


    # get entire forecast history
    def getdailycasts(self,locations:list,currentdate):

        woeids = self.getwoeids(locations)
        # get dailyforecasts per location
        lstdata= []
        for ind, woeid in enumerate(woeids):
            locforecast = {}
            response = requests.get("https://www.metaweather.com/api/location/{}/{}/{}/{}".format(woeid,currentdate.year,currentdate.month,currentdate.day))
            # turn  response into string
            redata= response.text
            # why use json loads
            data = json.loads(redata)
            locforecast["cast"] = data
            locforecast["location"] = locations[ind]
            lstdata.append(locforecast)
        return lstdata

    # create objects per forecast
    def dataparser(self,citycast:list,description):



        if description == "forecast":
            lstforecasts = []
            # create list of forecast objects
            for city in citycast:
                for row in city["consolidated_weather"]:       
                    lstforecasts.append(forecast(row["id"],row["weather_state_name"],row["weather_state_abbr"],row["wind_direction_compass"],\
                    row["created"],row["applicable_date"],row["min_temp"],row["max_temp"],row["the_temp"],row["wind_speed"],row["wind_direction"],\
                    row["air_pressure"],row["humidity"],row["visibility"],row["predictability"],city["time"],city["sun_rise"],city["sun_set"],\
                    city["timezone_name"],city["title"],city["location_type"],city["woeid"],city["latt_long"],city["timezone"]))
            return lstforecasts

                 
         
        elif description == "dailycast":

            lstdailycasts = []
            for city in citycast:
                for row in city["cast"]:
                    lstdailycasts.append(dailycast(row["id"],city["location"],row["weather_state_name"],row["weather_state_abbr"],row["wind_direction_compass"],\
                    row["created"],row["applicable_date"],row["min_temp"],row["max_temp"],row["the_temp"],row["wind_speed"],row["wind_direction"],\
                    row["air_pressure"],row["humidity"],row["visibility"],row["predictability"]))     

            return lstdailycasts
        else:
            return "Unrecognized data description"


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









