import datetime
import time
import requests
from plyer import notification

covid_data = None
try:
    covid_data = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:
    print("pls check internet connection")

if covid_data != None:
    data = covid_data.json()['Success']
    while True:
        notification.notify(
            title="COVID19 Stats on {}".format(datetime.date.today()),
            message="Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                totalcases=data['cases'],
                todaycases=data['todayCases'],
                todaydeaths=data['todayDeaths'],
                active=data["active"]),
            app_icon="./virus.ico",
            timeout=30

        )
        time.sleep(60 * 60 * 4)
