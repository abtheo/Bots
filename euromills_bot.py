#Runtime: 4pm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from time import sleep
from winner import send_winner_mail
import random
import pathlib
import json

birthday = "01/01/97" 

config = ""
with open(str(pathlib.Path(__file__).parent) + '/config.json') as config_file:
    config = json.load(config_file)
        
#Load Firefox profile
profile = webdriver.FirefoxProfile("C:/Users/GE60 2PE/AppData/Roaming/Mozilla/Firefox/Profiles/wqatwvdj.default-release")
driver = webdriver.Firefox(firefox_profile=profile,executable_path="D:/Bots/bin/geckodriver.exe")

#Get
driver.get("https://www.euro-millions.com/sign-in")

#Let page load
sleep(2)

#Fill Login form
driver.find_element_by_css_selector("input#Email").send_keys("george.steel92@gmail.com")
driver.find_element_by_css_selector("input#Password").send_keys(config['euro_password'])
driver.find_element_by_css_selector("input#Submit").submit()

#Enter Daily Lotto
driver.get("https://www.euro-millions.com/free-lottery/play?lottery=daily")
sleep(2)

driver.find_element_by_css_selector("input[value='Quick Pick']").click()
sleep(2)
driver.find_element_by_css_selector("input#submit_ticket").click()

#Close and exit
driver.close()
exit()

"""TODO: Results checking"""
# sleep(15)
# driver.get("https://www.euro-millions.com/results-checker")

# if birthday in winner_bday:
#     send_winner_mail(f"Won the Birthday Lottery! {winner_bday}")

