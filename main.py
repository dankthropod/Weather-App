import requests
import json
import replit
from datetime import datetime
import time
import selenium
from selenium import webdriver

starttime = time.time()

run = True

api_key = 'd8f89bd539dd3708a7a3a1cb7febecd3'
lat = 36.7212
lon = -4.4217

url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

def fetchWeather():
  replit.clear()
  now = datetime.now()
  currentTime = now.strftime("%H:%M:%S")
  
  response = requests.get(url)
  data = json.loads(response.text)

  currentTemp = data["current"]["temp"]
  currentFeelTemp = data["current"]["feels_like"]
  currentHumidity = data["current"]["humidity"]
  currentWindSpeed = data["current"]["wind_speed"]
  currentWindDir = data["current"]["wind_deg"]

  print(f"The time is {currentTime} UTC, and it is {currentTemp} degrees celsius outside right now.\nThe temperature feels like {currentFeelTemp} degrees. The humidity is {currentHumidity}%.\nThe wind: The wind is blowing at {currentWindSpeed}m/s and at {currentWindDir}º degrees\n")
  #stop = input("Say stop to stop")
  #if(stop == "stop"):
  #  run == False
  #  replit.clear

  time.sleep(60.0)

def fetchImage():
  browser = webdriver.Firefox()
  browser.get('http://openweathermap.org/weathermap?basemap=satellite&cities=false&layer=precipitation&lat=39.3003&lon=4.9219&zoom=6')
  time.sleep(5)             
  browser.save_screenshot('screenie.png')
  browser.quit()

while run == True:
#  fetchImage()
  fetchWeather()
