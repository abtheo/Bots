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
        
#Init and connect to homepage
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)   
driver.get("https://winadinner.com/daily-draw/")

#Let page load
sleep(2)

#Login button click
driver.find_element_by_css_selector(".signin-menu .reverse").click()

#Fill Login form
driver.find_element_by_id("user_name").send_keys("george.steel92@gmail.com")
driver.find_element_by_id("password").send_keys(config['dinner_password'])
driver.find_element_by_id("sign-in-submit").submit()

#WIP: Wait for registration