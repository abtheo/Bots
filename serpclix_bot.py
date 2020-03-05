
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from time import sleep
import random

#Load Firefox profile
profile = webdriver.FirefoxProfile("C:/Users/georg/AppData/Roaming/Mozilla/Firefox/Profiles/ul5p82rs.default-release")
profile.add_extension("C:/Users/georg/AppData/Roaming/Mozilla/Firefox/Profiles/ul5p82rs.default-release/extensions/dev@serpclix.com.xpi")   
profile._install_extension("C:/Users/georg/AppData/Roaming/Mozilla/Firefox/Profiles/ul5p82rs.default-release/extensions/dev@serpclix.com.xpi")
profile.set_preference("browser.privatebrowsing.autostart", False)
profile.set_preference('browser.preferences.instantApply', True)
profile.set_preference( "privacy.clearOnShutdown.offlineApps", False )
profile.update_preferences()

driver = webdriver.Firefox(firefox_profile=profile,
                           executable_path="C:/Bots/bin/geckodriver.exe",
                           log_path='C:/Bots/logs/serpclix.log')
#Load client
driver.start_client()
sleep(30)
print("Going...")

def main():
    
    driver.get("moz-extension://35c4befe-a8cc-4ae7-a938-6eb717f6c0ae/html/orders.html")
    window_before = driver.window_handles[0]
    #Polling loop
    while True:
        sleep(2)
        print('Polling Loop:')
        try:
            #Click Notification
            orders = driver.find_elements_by_css_selector("html > body.orders > div#serpclix_orders_list_app > ul#orders > li")
            order = random.choice(orders)
            print('found order')
            order.click()
            sleep(2)
            
            #Switch window
            window_after = driver.window_handles[1]
            driver.switch_to_window(window_after)

            #Select Google Searchbar & Paste keyword
            sleep(6)
            bar = driver.find_element_by_css_selector(".gLFyf")
            
            if bar == None:
                raise Exception()

            bar.click()
            sleep(1)
            bar.send_keys(Keys.CONTROL, 'v', Keys.ENTER)
            sleep(1)
            break
        
        except Exception as e:
            print(e)
            sleep(5)
            print('trying again...')
            #Sleep 5 mins if no notification
            #sleep(60 * 5)


    #Loop until correct page
    clickFlag = False
    while not clickFlag:
        try:
            sleep(4)
            print('Looking...')
            search_results = driver.find_elements_by_css_selector(".srg .g .r")
            sleep(4)
            #Loop Searches on Page
            for search in search_results:
                divstyle = search.get_attribute("style")
                if "rgb" in divstyle:
                    print('Hooray!')
                    atag = search.find_element_by_tag_name("a")
                    sleep(1)
                    atag.click()
                    #Sit on page for a while
                    sleep(360)
                    clickFlag = True
                    break

        #Else No luck, iterate pages until we find it
            if not clickFlag:
                print("No coloured element found, moving to next page")
                sleep(2)
                driver.find_element_by_id("pnnext").click()
                sleep(2)
        except Exception as e:
            print(e)
            continue


    sleep(5)
    driver.switch_to_window(window_before)
    sleep(2)
    driver.get("moz-extension://35c4befe-a8cc-4ae7-a938-6eb717f6c0ae/html/orders.html")
    sleep(2)
while True:
    print('running main')
    main()
    sleep(120)


"""
If we need to start the addon programatically:
#driver.start_session()
# driver.get("about:addons")
# sleep(5)
# #driver.find_element_by_css_selector(".addon-name-link").click()
# driver.find_element_by_tag_name("addon-card").click()

# elem = driver.find_element_by_css_selector("window#addons-page > stack#main-page-stack *> #html-view-browser")
# print(elem)

# #driver.switch_to.frame(elem)
# sleep(1)
# btn = driver.find_element_by_xpath("/html/body/div/div/addon-list/section[1]/addon-card[2]/div/div/div/div/input")
# btn2 = elem.find_element_by_xpath("/html/body/div/div/addon-list/section[1]/addon-card[2]/div/div/div/div/input")
# print(btn)
# print(btn2)
# driver.find_element_by_css_selector("#main > div:nth-child(1) > addon-list:nth-child(1) > section:nth-child(2) > addon-card:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input:nth-child(5)").click()

# driver.get("moz-extension://2f128f20-0700-4e63-a272-9d70072b6b31/html/orders.html")

"""
