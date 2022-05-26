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




class dailycast(db.Model):

    __tablename__ = "forecast"
    # define 1class attributes to table columns
    Id = db.Column(db.Integer, primary_key=True, autoincrement=False)
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
    Location = db.Column(db.String(50), nullable=False)

    def __init__(self,Id,Location,WeatherState,WeatherStateAbbr,WindDirectionCompass,CreatedDate,ForecastDate,MinTemp,MaxTemp,RealTemp,WindSpeed,\
        WindDirection,AirPressure,Humidity,Visibility,Predictability):

        self.Id = Id
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
        self.Location = Location

    def __repr__(self):
        return f"dailycast('{self.Id}','{self.ForecastDate}','{self.Location}')"




 