#NOTE: This program works for python2 & python3
#Suppose if there is any error, especially with urllib (uncomment), try running with python2
#You must have created your DB before executing this program

from flask import Flask
import pymysql

#Library to access external APIs (NOTE: This may not work with python3)
#from urllib.request import urlopen

#For Python3 only
import requests


#Read OpenWeatherMap API usage here - https://openweathermap.org/api/one-call-api

#Insert your OpenWeatherMap API here
OPEN_WEATHER_MAP_API_KEY = "95c24917f8cc445dad4ea6113a933807"

#give your Lattitude and Longitude
lat = '8.01'
lon = '77.05'

#Create openweathermap url
api_url = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(lon)+"&exclude=hourly,daily,minutely,alerts+&appid="+OPEN_WEATHER_MAP_API_KEY+"&units=metric"
 
app = Flask(__name__)
@app.route('/fetchWeather')
def get_open_weather_map_data():
  
  #For Python2
  #response = urlopen(api_url).read()
  
  #For Python3
  response = requests.get(api_url).json()
  
  print(response)
  return response

 #To save API response to mySQL
@app.route('/todb')
def todb():
 
 #receiving data from OpenWeatherMap
 response = requests.get(api_url).json()
 
 #Cleaning the data to make it look tidy
 currentWeather = response['current']
 weatherReport = currentWeather['weather'][0]
 
 #Connect to MySQL DB (Not tested, May have errors!)
 conn = pymysql.connect(database="WeatherDB",user="admin",password="admin",host="localhost")
 cur=conn.cursor()
 
 #Table 1 shows realtime weather
 cur.execute("INSERT INTO currentWeatherTable (clouds, dew_point, dt, feels_like, humidity, temp ) VALUES (%(clouds)s, %(dew_point)s, %(dt)s, %(feels_like)s, %(humidity)s, %(temp)s )",currentWeather)
 
 #Table 2 shows summary
 cur.execute("INSERT INTO weatherSummaryTable (id, description, icon, main) VALUES (%(id)s, %(description)s, %(icon)s, %(main)s)",weatherReport)
 return currentWeather

if __name__ == "__main__":
  #Application runs on port 3000
  app.run(host="0.0.0.0", port='3000', debug=1)
