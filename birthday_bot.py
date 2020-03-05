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

birthday = "01/01/97" 

config = ""
with open(str(pathlib.Path(__file__).parent) + '/config.json') as config_file:
    config = json.load(config_file)

#Load Firefox profile
profile = webdriver.FirefoxProfile("C:/Users/georg/AppData/Roaming/Mozilla/Firefox/Profiles/ul5p82rs.default-release")
driver = webdriver.Firefox(firefox_profile=profile,
                           executable_path="C:/Bots/bin/geckodriver.exe",
                           log_path='C:/Bots/logs/birthday.log')
      
#Init and connect to homepage
  
driver.get("https://www.freebirthdatelottery.com/birthdate-draw/")

#Let page load
sleep(2)

#Login button click
driver.find_element_by_css_selector(".hentry.page.post-13.status-publish.type-page a").click()
sleep(2)
#Fill Login form
driver.find_element_by_css_selector("input#user_login").send_keys("george.steel92@gmail.com")
driver.find_element_by_css_selector("input#user_pass").send_keys(config['birthday_password'])
driver.find_element_by_css_selector("input#wp-submit").submit()
sleep(5)

#Check Birthday
driver.get("https://www.freebirthdatelottery.com/birthdate-draw/")

winner_bday = driver.find_element_by_css_selector(".checkresults.fullwidthbox.resultbox > h1").text

if birthday in winner_bday:
    send_winner_mail(f"Won the Birthday Lottery! {winner_bday}")

#Close and exit
driver.close()
exit()
