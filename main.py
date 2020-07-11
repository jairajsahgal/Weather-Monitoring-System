#libraries imported
import requests
import time as waqt
import random
import pandas as pd
import datetime
import json

#Processing
weather_info={"City Name":[],"Temp":[],"Date":[],"Time":[]}
cities=input("Enter Multiple City Names").strip().split()
change="C"
try:
	while(int(input("For stopping Enter 0, else to keep running Enter any number between 1 to 9 "))):
	  for city in cities:
	  	# print("Temperature of city :",city)
	    data=requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=108ae6197aac65ad35144a43f5cb6a6d".format(city)).json()
	    change=input("Temperature in Celcius (C) or Fahrenheit (F) ")
	    if change=="C" or change=='c':
	      print("Temperature",data['main']['temp'],"C")
	      weather_info["Temp"].append(str(data['main']['temp'])+" C")
	      weather_info["City Name"].append(data["name"])
	      weather_info["Date"].append(datetime.datetime.now().strftime("%d-%m-%Y"))
	      weather_info["Time"].append(datetime.datetime.now().strftime("%H:%M:%S"))
	    elif change=='F' or change=='f':
	      print("Temperature",str(round(((data['main']['temp']*1.8)+32),2)),"F")
	      weather_info["Temp"].append(str(round(((data['main']['temp']*1.8)+32),2))+" F")
	      weather_info["City Name"].append(data["name"])
	      weather_info["Date"].append(datetime.datetime.now().strftime("%d-%m-%Y"))
	      weather_info["Time"].append(datetime.datetime.now().strftime("%H:%M:%S"))
	    else:
	      break
	    waqt.sleep(random.randint(1,10))
except Exception(e):
	print(e)


	    

#for sheet 2
f = open('city_list.json') 

# returns JSON object as 
# a dictionary 
data = json.load(f) 
possible_city=[]
for i in data:
	possible_city.append(i['name'])
f.close()

extra_info="I have used my own api id and it can only process 1,00,000\n Also I have added time and date to get more detail from the excel sheet.\nThe time and date is taken from the local machine."
with pd.ExcelWriter('output.xlsx') as writer:  
    pd.DataFrame(weather_info).to_excel(writer, sheet_name='Sheet 1')
    pd.DataFrame({'City Name':possible_city}).to_excel(writer, sheet_name='Sheet 2')
    pd.DataFrame({'Extra Info':extra_info.split("\n")}).to_excel(writer, sheet_name='Sheet 3')
