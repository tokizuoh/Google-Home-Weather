import TokyoWeather
import SeleniumMp3
import GoogleHome
import pychromecast

### Google Homeをあらかじめ接続しておく ###
chromecasts = pychromecast.get_chromecasts()
google_home = chromecasts[0]

### OpenWeatherMap ###
message = TokyoWeather.Weather_API()
print(message)

### messageをmp3に ###
url = SeleniumMp3.Texr_Exchange_Mp3(message)
print(url)

###Google Home###
GoogleHome.Play_Mp3(google_home, url)
