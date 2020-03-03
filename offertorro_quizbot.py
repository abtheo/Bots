from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from winner import send_winner_mail
import json
import pathlib

profile = webdriver.FirefoxProfile("C:/Users/GE60 2PE/AppData/Roaming/Mozilla/Firefox/Profiles/wqatwvdj.default-release")
driver = webdriver.Firefox(firefox_profile=profile,executable_path="D:/Bots/bin/geckodriver.exe")

driver.get("https://earnably.com/earn/offertoro")