#Runtime: 4pm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
                           log_path='C:/Bots/logs/autosurf.log')

#Manual click pages
sites = ["http://www.ebesucher.com/c/games-clans?surfForUser=georgesteel92",
         "http://www.ebesucher.com/c/sport?surfForUser=georgesteel92",
         "http://www.ebesucher.com/c/animals-pets?surfForUser=georgesteel92",
         "http://www.ebesucher.com/c/auctions?surfForUser=georgesteel92",
         "http://www.ebesucher.com/c/shopping-e-commerce?surfForUser=georgesteel92",
         "http://www.ebesucher.com/c/jobs-business?surfForUser=georgesteel92",
         "http://www.ebesucher.com/c/adult-content?surfForUser=georgesteel92",
         "http://www.ebesucher.com/c/things-for-free?surfForUser=georgesteel92",
         "http://www.ebesucher.com/c/fun-entertainment?surfForUser=georgesteel92",
         "http://www.ebesucher.com/c/earn-money-mlm?surfForUser=georgesteel92",
         "http://www.ebesucher.com/c/telecommunication-mobile?surfForUser=georgesteel92",
         "http://www.ebesucher.com/c/car-motorcycle?surfForUser=georgesteel92",
         "http://www.ebesucher.com/c/computers-accessories?surfForUser=georgesteel92"]

#Get
while True:
    for site in sites:
        #sleep(123)
        try:
            #Goto Ad Wall
            driver.get(site)
            sleep(2)
            
            #window_before = driver.window_handles[0]    
            sleep(2)

            #Click random ad
            items = driver.find_elements_by_css_selector('.item.clickAd')
            for choice in items:
                driver.execute_script("arguments[0].scrollIntoView();", choice)
                sleep(2)
                choice.click()
                print("Click successful! Sleeping...")
                #Await finish
                sleep(180)#
                print("Attempting kill...")
                handles = driver.window_handles
                if len(handles) > 1:
                    driver.switch_to.window(handles[1])
                    driver.close()
                    driver.switch_to.window(handles[0])
                    print("Kill successful!")
                else:
                    print("New window not detected, continuing anyway...")
                                                

            #No more items in current page            
            print("No items remaining.")

        except Exception as e:
            print(e)
            #sleep(290)
            continue

                    
    #Checked 'em all, wait for new offers
    sleep(360)
