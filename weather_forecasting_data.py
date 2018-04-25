import re
import urllib.request
printable_final=""
#this is weather forcast data parser code
#https://www.weather-forecast.com/locations/Espoo/forecasts/latest
location=input("Which city's weather you want to know?\n")
url="https://www.weather-forecast.com/locations/" +location+ "/forecasts/latest"
raw_data=urllib.request.urlopen(url).read()
utf_data=raw_data.decode('utf-8')
weather_chunk=re.search('span class="phrase"', utf_data)
#start_position_one=st1/end_postion_one=ed1
st1=weather_chunk.start()
ed1=weather_chunk.end()+12
##privatized weather data=p_weather_data
p_weather_data=utf_data[st1:ed1]
###get the actual data position in the html documnet
st2=weather_chunk.end()+1
ed2=weather_chunk.end()+300
printable=utf_data[st2:ed2]
##l1=printable.find("total")-1
##printable_final=printable[0:l1]
local=re.search("</span>", printable)
ed3=local.start()-2
pritable_final=printable[0:ed3]
print("The weather forecast information for " +location+ " today is " +pritable_final+".")















 
