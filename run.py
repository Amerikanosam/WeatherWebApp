from weatherapp import app
from weatherapp.datahandler import datahandler
from datetime import datetime

if __name__ == '__main__':
    

    lstlocations = ["London","Seattle","San Francisco"]
    datamanager = datahandler()
    data = datamanager.getforecast(lstlocations)
    forecasts = datamanager.dataparser(data)
    datamanager.insertdata(forecasts)

    # get data on current date
    #castdata = datamanager.getdailycasts(lstlocations,datetime.utcnow())
    #dailyforecasts = datamanager.dataparser(castdata,"dailycast")
    #datamanager.insertdata(dailyforecasts)



    app.run()
