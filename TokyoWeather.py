import sys
import requests
import json
import time

def Weather_API():
    #OpenWeatherMapから天候情報をAPIで持ってきてjsonで保存
    city_name = "Tokyo"
    API_KEY = "-"
    api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"
    url = api.format(city = city_name, key = API_KEY)
    response = requests.get(url)
    data = response.json()
    jsonText = json.dumps(data, indent=4)
    A = json.loads(jsonText)

    # jsonのdtから日付変換してjsonに変更を反映させる
    now = time.ctime(A["dt"])
    cnvtime = time.strptime(now)
    sc_time = time.strftime("%Y%m%d%H%M", cnvtime)
    A["dt"] = sc_time

    hour = A["dt"][8:10]
    minute = A["dt"][10:]

    message = hour + "時" + minute + "分" + "現在の" + A["name"] + "の" + \
              "平均気温は" + str(A["main"]["temp"]) + "度、" + \
              "最高気温は" + str(A["main"]["temp_max"]) + "度、" + \
              "最低気温は" + str(A["main"]["temp_min"]) + "度です。" + \
              "湿度は" + str(A["main"]["humidity"]) + "パーセントです。" + \
              "気圧は" + str(A["main"]["pressure"]) + "ヘクトパスカルです。" + \
              "風速は秒速" + str(A["wind"]["speed"]) + "メートルです。"

    return message
