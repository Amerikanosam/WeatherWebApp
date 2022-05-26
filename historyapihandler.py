import requests
import datahandler
from datetime import datetime
import json
import pandas as pd

class datahandler():
    
    def __init__(self):
        pass

    def getwoeid(self,location):

        # get woeid for each location
        response = requests.get("https://www.metaweather.com/api/location/search/",params={"query":location})
        data = response.text
        jsdata = json.loads(data)[0]
        #transform response to json object
        return  jsdata["woeid"]

    def getforecasts(self,woeid,currentdate):
        
        # get request for specific woeid
        
        response = requests.get("https://www.metaweather.com/api/location/{}/{}/{}/{}".format(woeid,currentdate.year,currentdate.month,currentdate.day))
        # turn  response into string
        redata= response.text
        data = json.loads(redata)
        return data

    # parse data into pandas for SQL db
    def dataparser(self,parseddata:list,location):
       
        forecastdf = pd.DataFrame(data=parseddata)
        forecastdf["location"] = location
        forecastdf["visibility"] = forecastdf["visibility"].fillna(0)
        return forecastdf

    def insertdata(self,cursor,data,tablename):
        # insert data from dataframe into SQL Server
    
        for index, row in data.iterrows():
            cursor.execute(
            "INSERT INTO {} (ID,Location,WeatherState,WeatherStateAbbr,WindDirectionCompass,CreatedDate,ForecastDate,MinTemp,MaxTemp,RealTemp,WindSpeed,WindDirection,AirPressure,Humidity,Visibility,Predictability)"
            "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)".format(tablename),
            row.id, row.location,row.weather_state_name, row.weather_state_abbr, row.wind_direction_compass, row.created,
            row.applicable_date,
            row.min_temp, row.max_temp, row.the_temp, row.wind_speed, row.wind_direction, row.air_pressure,
            row.humidity, row.visibility, row.predictability)
        