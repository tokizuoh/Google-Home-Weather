from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
import requests


def Texr_Exchange_Mp3(message):
    driver = webdriver.Chrome(executable_path = "\\chromedriver.exe")
    driver.get("https://soundoftext.com/")

    elem_t = driver.find_element_by_class_name("field__textarea")   #element_text
    elem_t.send_keys(message)

    elem_c = driver.find_element_by_class_name("field__select")   #element_country
    elem_c_s = Select(elem_c)   #element_country_select
    elem_c_s.select_by_value("ja-JP")

    driver.find_element_by_class_name("field__submit").click()   #Submit_button

    sleep(1)
    
    driver.execute_script("window.scrollTo(20, document.body.scrollHeight);")

    sleep(5)

    url = str(driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div[2]/a[2]').get_attribute('href'))
    
    if url == "None":
        print("The URL could not be obtained. I will get it again.")
        Texr_Exchange_Mp3(message)
    else:
        driver.quit()
        return url
