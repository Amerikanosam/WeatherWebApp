from weatherapp import db

# create class for weather forecast
class forecast(db.Model):
    __tablename__ = "WeatherForecast"
    # define class attributes to table columns
    ForecastID = db.Column(db.Integer, primary_key=True, autoincrement=False)
    WeatherState = db.Column(db.String(20),nullable=False)
    WeatherStateAbbr = db.Column(db.String(5), nullable=False)
    WindDirectionCompass = db.Column(db.String(3))
    CreatedDate = db.Column(db.DateTime, nullable=False)
    ForecastDate = db.Column(db.Date, nullable=False)
    MinTemp = db.Column(db.Float)
    MaxTemp = db.Column(db.Float)
    RealTemp = db.Column(db.Float)
    WindSpeed = db.Column(db.Float)
    WindDirection= db.Column(db.Float)
    AirPressure = db.Column(db.Float)
    Humidity = db.Column(db.Integer)
    Visibility = db.Column(db.Float)
    Predictability = db.Column(db.Integer)
    LocationTime = db.Column(db.DateTime, nullable = False)
    SunRise = db.Column(db.DateTime,nullable=False)
    SunSet = db.Column(db.DateTime, nullable=False)
    TimeZoneName = db.Column(db.String(50), nullable=False)
    ForecastLocation = db.Column(db.String(50), nullable=False)
    LocationType = db.Column(db.String(20), nullable=False)
    Woeid = db.Column(db.Integer,nullable=False)
    Lat_Long = db.Column(db.String(200), nullable=False)
    TimeZone = db.Column(db.String(50), nullable=False)



    def __init__(self,ForecastID,WeatherState,WeatherStateAbbr,WindDirectionCompass,CreatedDate,ForecastDate,MinTemp,MaxTemp,RealTemp,\
        WindSpeed,WindDirection, AirPressure,Humidity,Visibility,Predictability,LocationTime,SunRise,SunSet,\
        TimeZoneName,ForecastLocation,LocationType, Woeid,Lat_Long,TimeZone):
    
        self.ForecastID = ForecastID
        self.WeatherState = WeatherState
        self.WeatherStateAbbr = WeatherStateAbbr
        self.WindDirectionCompass = WindDirectionCompass
        self.CreatedDate = CreatedDate
        self.ForecastDate = ForecastDate
        self.MinTemp = MinTemp
        self.MaxTemp = MaxTemp
        self.RealTemp = RealTemp
        self.WindSpeed = WindSpeed
        self.WindDirection = WindDirection
        self.AirPressure = AirPressure
        self.Humidity = Humidity
        self.Visibility = Visibility
        self.Predictability = Predictability
        self.LocationTime = LocationTime
        self.SunRise = SunRise
        self.SunSet = SunSet
        self.TimeZoneName = TimeZoneName
        self.ForecastLocation = ForecastLocation
        self.LocationType = LocationType
        self.Woeid = Woeid
        self.Lat_Long = Lat_Long
        self.TimeZone = TimeZone


    def __repr__(self):
        return f"forecast('{self.ForecastID}', '{self.ForecastDate}','{self.ForecastLocation}')"




class currentcast(db.Model):

    __tablename__ = "forecast"
    # define 1class attributes to table columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String(50),nullable=False)
    region = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100),nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    timezoneid = db.Column(db.String(50))
    lastupdated = db.Column(db.DateTime)
    lastupdatedepoch = db.Column(db.Integer)
    localtime = db.Column(db.DateTime)
    localtimeepoch = db.Column(db.Integer)
    weathertext = db.Column(db.String(50))
    tempC = db.Column(db.Float)
    tempF = db.Column(db.Float)
    feelslikeC = db.Column(db.Float)
    feelslikeF = db.Column(db.Float)
    windspeed_km = db.Column(db.Float)
    windspeed_m = db.Column(db.Float)
    winddirection = db.Column(db.String(10))
    windspeeddegree = db.Column(db.Integer)
    pressure_in = db.Column(db.Float)
    pressure_mb = db.Column(db.Float)
    humidity = db.Column(db.Integer)
    visibility_km = db.Column(db.Float)
    visibility_miles = db.Column(db.Float)
    precipitation_mm = db.Column(db.Float)
    precipitation_in = db.Column(db.Float)
    cloud = db.Column(db.Integer)
    uv = db.Column(db.Float)
    gust_kph = db.Column(db.Float)
    gust_mph = db.Column(db.Float)
    isday = db.Column(db.Boolean)


    def __init__(self,location,region,country,latitude,longitude,timezoneid,lastupdated,lastupdatedepoch,localtime,localtimeepoch,\
                weathertext,tempC,tempF,feelslikeC,feelslikeF,windspeed_km,windspeed_m,winddirection,windspeeddegree,pressure_in,pressure_mb,\
                humidity,visibility_km,visibility_miles,precipitation_mm,precipitation_in,cloud,uv,gust_kph,gust_mph,isday):

        self.location = location
        self.region = region
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.timezoneid = timezoneid
        self.lastupdated = lastupdated
        self.lastupdatedepoch = lastupdatedepoch
        self.localtime = localtime
        self.localtimeepoch = localtimeepoch
        self.weathertext = weathertext
        self.tempC = tempC
        self.tempF = tempF
        self.feelslikeC = feelslikeC
        self.feelslikeF = feelslikeF
        self.windspeed_km = windspeed_km
        self.windspeed_m = windspeed_m
        self.winddirection = winddirection
        self.windspeeddegree = windspeeddegree
        self.pressure_in = pressure_in
        self.pressure_mb = pressure_mb
        self.humidity = humidity
        self.visibility_km = visibility_km
        self.visibility_miles = visibility_miles
        self.precipitation_mm = precipitation_mm
        self.precipitation_in = precipitation_in
        self.cloud = cloud
        self.uv = uv
        self.gust_kph = gust_kph
        self.gust_mph = gust_mph
        self.isday = isday
                

    def __repr__(self):
        return f"dailycast('{self.localdate}','{self.location}')"




 