from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from winner import send_winner_mail
import json
import pathlib
import random
config = ""
with open(str(pathlib.Path(__file__).parent) + '/config.json') as config_file:
    config = json.load(config_file)
      
profile = webdriver.FirefoxProfile("C:/Users/GE60 2PE/AppData/Roaming/Mozilla/Firefox/Profiles/wqatwvdj.default-release")
#Headless Browser
options = webdriver.FirefoxOptions()
# options.add_argument('-headless')

driver = webdriver.Firefox(firefox_profile=profile,executable_path="D:/Bots/bin/geckodriver.exe", firefox_options=options)

driver.get("https://www.offertoro.com/click_track/track/19494520/963/94v27413q284/691/web/8/y/")
sleep(10)

q1 = driver.find_element_by_id("choice1")
q2 = driver.find_element_by_id("choice2")

if random.uniform(0,1) > 0.5:
    q1.click()
else:
    q2.click()


#driver.get("https://earnably.com/earn/offertoro")
#driver.find_element_by_css_selector("body > div > div.support-menu > ul > li:nth-child(3) > a").click()
# driver.get("https://moretvtime.com/article/website-and-dedicated-hosting-providers-have-it-all-under-one-roof?pr=16&h=46dea216&ph=f4baf6a1dce917df#")

# driver.close()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from winner import send_winner_mail
import json
import pathlib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
config = ""
with open(str(pathlib.Path(__file__).parent) + '/config.json') as config_file:
    config = json.load(config_file)
      
profile = webdriver.FirefoxProfile("C:/Users/GE60 2PE/AppData/Roaming/Mozilla/Firefox/Profiles/wqatwvdj.default-release")
#Headless Browser
options = webdriver.FirefoxOptions()
options.add_argument('-headless')

driver = webdriver.Firefox(firefox_profile=profile,executable_path="D:/Bots/bin/geckodriver.exe", firefox_options=options)

driver.get("https://www.offertoro.com/click_track/track/19494520/963/94v27413q284/691/web/8/y/")
sleep(10)
driver.find_elements_by_css_selector("html body div#body-content.zoom-50 div#progressbar.container.d-flex.align-items-center.content-box div.flex-grow-1 div#progressbar-value div.progress div#progressbar-text.blinking-text.text-center").click()


choice = None
if random.uniform(0,1) > 0.5:
    choice = "choice1"
else:
    choice = "choice2"
#Next1

for i in range(20):
    try:
        image = driver.find_element_by_class_name("sc-survey-choice-vote-stat")
        driver.execute_script("arguments[0].display = 'block';", image) 
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, choice))).click()
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.flex-1:nth-child(1)"))).click()
        # sleep(2)
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".sc-survey-navigation"))).click()
    except Exception as e:
        print(e)
print("Didn't die")
#driver.get("https://earnably.com/earn/offertoro")
#driver.find_element_by_css_selector("body > div > div.support-menu > ul > li:nth-child(3) > a").click()
# driver.get("https://moretvtime.com/article/website-and-dedicated-hosting-providers-have-it-all-under-one-roof?pr=16&h=46dea216&ph=f4baf6a1dce917df#")

# driver.close()