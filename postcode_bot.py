from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

from time import sleep
from winner import send_winner_mail
import random

postcode = 'SK10 3PX'

#Init and connect to postcode homepage
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.set_page_load_timeout(10)

counter = 0
#Try catch timeouts, 5 times
while counter < 5:
    try:
        driver.get("https://pickmypostcode.com/stackpot/?postcode=SK10+3PX&email=george.steel92\%40gmail.com#")

        #Let page load
        sleep(2)

        #Get Stackpot winners
        stackpot_results = driver.find_elements_by_css_selector("p.result--postcode")

        #Search winners for our postcode
        for result in stackpot_results:
            if postcode in result.text:
                print("Stackpot Winner!")
                send_winner_mail(f"Won the Postcode Lottery Stackpot! {result.text}")
                sleep(2)

        #Go to main draw page
        driver.get("https://pickmypostcode.com/?postcode=SK10+3PX&email=george.steel92\%40gmail.com#")
        sleep(2)

        #Click away the fucking Cookies notice
        driver.find_element_by_css_selector("button.qc-cmp-button").click()
        driver.find_element_by_css_selector("button.qc-cmp-button.qc-cmp-save-and-exit").click()

        #Get results of main draw
        maindraw_result = driver.find_element_by_css_selector("p.result--postcode")
        if postcode in maindraw_result.text:
            print("Main Draw Winner!")
            send_winner_mail(f"Won the Postcode Lottery Main Draw! {maindraw_result.text}")
            sleep(2)


        #Go to Survery Draw
        # driver.get("https://pickmypostcode.com/survey-draw/?postcode=SK10+3PX&email=george.steel92\%40gmail.com#")
        #Find radio button answers
        # survey_btns = driver.find_elements_by_css_selector(".questions >* .radio > input")
        # #Click random answer
        # random.choice(survey_btns).click()
        #Submit Survey
        # driver.find_element_by_css_selector(".btn.btn__xs.btn-loader").click()

        #Go to Video Draw
        driver.get("https://pickmypostcode.com/video/?postcode=SK10+3PX&email=george.steel92\%40gmail.com#")
        
        driver.find_element_by_css_selector(".brid-overlay-play-button.brid-button").click()

        #Waiting for element to appear 
        sleep(60)
        video_result = driver.find_element_by_css_selector("p.result--postcode")
        if postcode in video_result.text:
            print("Video Draw Winner!")
            send_winner_mail(f"Won the Postcode Lottery Video Draw! {video_result.text}")
            sleep(2)


        #Finished, end loop
        break
    except TimeoutException as te:
        print(te)
        print("Trying again...")
        counter += 1


#End session
driver.close()
exit()