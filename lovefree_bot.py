#Runtime: 4pm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

from time import sleep
from winner import send_winner_mail
import random
import pathlib
import json

name = "George92"

config = ""
with open(str(pathlib.Path(__file__).parent) + '/config.json') as config_file:
    config = json.load(config_file)
        
#Load Firefox profile
profile = webdriver.FirefoxProfile("C:/Users/GE60 2PE/AppData/Roaming/Mozilla/Firefox/Profiles/wqatwvdj.default-release")
driver = webdriver.Firefox(firefox_profile=profile,executable_path="D:/Bots/bin/geckodriver.exe")

#Get
driver.get("https://lovefreelotto.com/ticket.php")

#Let page load
sleep(2)

#Login button click
driver.find_element_by_css_selector("button#quickpick").click()
sleep(1)

#Fill Login form
driver.find_element_by_css_selector("input#emailaddress").send_keys("george.steel92@gmail.com")
driver.find_element_by_css_selector("input#emailv").send_keys("george.steel92@gmail.com")
driver.find_element_by_css_selector("button#ticket-submit").submit()

#Confirm Ticket
sleep(10)
driver.find_element_by_css_selector("button#submitButton").click()

counter = int(''.join(filter(str.isdigit, driver.current_url)))

while counter < 14:
    #Pick again
    driver.find_element_by_css_selector("button#quickpick").click()
    sleep(1)

    #Submit
    driver.find_element_by_css_selector("button#ticket-submit").submit()

    #Confirm Ticket
    sleep(8)
    driver.find_element_by_css_selector("button#submitButton").click()

#Close and exit
driver.close()
exit()

