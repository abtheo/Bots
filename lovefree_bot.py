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
profile = webdriver.FirefoxProfile("C:/Users/georg/AppData/Roaming/Mozilla/Firefox/Profiles/ul5p82rs.default-release")
driver = webdriver.Firefox(firefox_profile=profile,
                           executable_path="C:/Bots/bin/geckodriver.exe",
                           log_path='C:/Bots/logs/lovefree.log')
#Get
driver.get("https://lovefreelotto.com/ticket.php")

#Let page load
sleep(2)

#Login button click
driver.find_element_by_css_selector("button#quickpick").click()
sleep(5)

#Fill Login form
#driver.find_element_by_css_selector("input#emailaddress").send_keys("george.steel92@gmail.com")
#driver.find_element_by_css_selector("input#emailv").send_keys("george.steel92@gmail.com")
driver.find_element_by_css_selector("button#ticket-submit").submit()

#Confirm Ticket
sleep(20)
driver.find_element_by_css_selector("button#submitButton").click()

counter = int(''.join(filter(str.isdigit, driver.current_url)))

while True:
    print('Looping...')
    try:
        #Pick again
        driver.find_element_by_css_selector("button#quickpick").click()
        sleep(1)

        #Submit
        driver.find_element_by_css_selector("button#ticket-submit").submit()

        #Confirm Ticket
        sleep(20)
        driver.find_element_by_css_selector("button#submitButton").click()

        sleep(5)
        counter = int(''.join(filter(str.isdigit, driver.current_url)))
        if counter > 14:
            break
        if 'thankyou' in driver.current_url:
            break
    except:
        print(e)
#Close and exit
driver.close()
exit()

