
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

from time import sleep
from winner import send_winner_mail
import random
import pathlib
import json
 # for adblockplus

#Load Firefox profile
profile = webdriver.FirefoxProfile("C:/Users/GE60 2PE/AppData/Roaming/Mozilla/Firefox/Profiles/wqatwvdj.default-release")
profile.add_extension("C:/Users/GE60 2PE/AppData/Roaming/Mozilla/Firefox/Profiles/wqatwvdj.default-release/extensions/dev@serpclix.com.xpi")
profile._install_extension("C:/Users/GE60 2PE/AppData/Roaming/Mozilla/Firefox/Profiles/wqatwvdj.default-release/extensions/dev@serpclix.com.xpi")
profile.set_preference("browser.privatebrowsing.autostart", False)
profile.set_preference('browser.preferences.instantApply', True)
profile.set_preference( "privacy.clearOnShutdown.offlineApps", False )
profile.update_preferences()

driver = webdriver.Firefox(firefox_profile=profile,executable_path="D:/Bots/bin/geckodriver.exe")

#Load client
#driver.get("moz-extension://2f128f20-0700-4e63-a272-9d70072b6b31/html/orders.html")
driver.start_client()
sleep(25)
print("Going...")
driver.get("moz-extension://2f128f20-0700-4e63-a272-9d70072b6b31/html/orders.html")
driver.get("moz-extension://2f128f20-0700-4e63-a272-9d70072b6b31/html/orders.html")
driver.get("moz-extension://2f128f20-0700-4e63-a272-9d70072b6b31/html/orders.html")



#driver.start_session()
# driver.get("about:addons")
# sleep(5)
# #driver.find_element_by_css_selector(".addon-name-link").click()

# elem = driver.find_element_by_css_selector("window#addons-page > stack#main-page-stack *> #html-view-browser")
# print(elem)

# #driver.switch_to.frame(elem)
# sleep(1)
# btn = driver.find_element_by_xpath("/html/body/div/div/addon-list/section[1]/addon-card[2]/div/div/div/div/input")
# btn2 = elem.find_element_by_xpath("/html/body/div/div/addon-list/section[1]/addon-card[2]/div/div/div/div/input")
# print(btn)
# print(btn2)
# driver.find_element_by_css_selector("#main > div:nth-child(1) > addon-list:nth-child(1) > section:nth-child(2) > addon-card:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input:nth-child(5)").click()

# driver.find_element_by_tag_name("addon-card").click()
#Click Notification
sleep(3)
driver.find_element_by_css_selector("html > body.orders > div#serpclix_orders_list_app > ul#orders").click()
sleep(5)
# #Select Google Searchbar & Paste keyword
driver.find_element_by_css_selector(".gLFyf.gsfi").send_keys(Keys.CONTROL, 'v').send_keys(Keys.ENTER)