import TokyoWeather
import SeleniumMp3
import GoogleHome

from time import sleep

### OpenWeatherMap ###
message = TokyoWeather.Weather_API()
print(message)

### messageをmp3に ###
url = SeleniumMp3.Texr_Exchange_Mp3(message)
print(url)

###Google Home###
GoogleHome.Play_Mp3(url)
