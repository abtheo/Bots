from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from winner import send_winner_mail
import json
from datetime import datetime
import pathlib

config = ""
with open('C:/Bots/config.json') as config_file:
    config = json.load(config_file)

#Coding with emojis LOL
winners = ["😍","😜","💩","🤑","😂"]

#Init and connect to emoji homepage
#Load Firefox profile
profile = webdriver.FirefoxProfile("C:/Users/georg/AppData/Roaming/Mozilla/Firefox/Profiles/ul5p82rs.default-release")
driver = webdriver.Firefox(firefox_profile=profile,
                           executable_path="C:/Bots/bin/geckodriver.exe",
                           log_path='C:/Bots/logs/emoji.log')

driver.get("https://freemojilottery.com/")

#Let page load
sleep(2)

#Click Login button
stackpot_results = driver.find_element_by_xpath("//a[@href='#login']").click()

#Fill Login form
driver.find_element_by_id("rnlr_user_login").send_keys("george.steel92@gmail.com")
driver.find_element_by_id("rnlr_user_pass").send_keys(config['emoji_password'])
driver.find_element_by_id("rnlr_login_submit").submit()
sleep(2)

#Scrape winning emojis
emojis = driver.find_elements_by_css_selector(".results-panel >* .emojione")

#Mail for win
if set(emojis) == set(winners):
    print("Won the Emoji Lottery Main Draw!")
    send_winner_mail("Won the Emoji Lottery Main Draw!")

#Check Fiver's Draw
driver.get("https://freemojilottery.com/fivers/")

#Get all winning rows
fivers_rows = driver.find_elements_by_css_selector("#fiversDraw >* .freemoji-display-name.clearfix")
for row in fivers_rows:
    #Find string of 5 emojis
    emojis = row.find_elements_by_css_selector(".emojione")
    
    #Mail winners
    if set(emojis) == set(winners):
        print("Won the Emoji Lottery Fiver Draw!")
        send_winner_mail("Won the Emoji Lottery Fiver Draw!")
        
#Close and exit
driver.close()

#Log last run time
with open('C:/Bots/logs/emoji_runs.log', "w") as logfile:
    logfile.write(str(datetime.now()))

exit()
