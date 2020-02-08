from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from winner import send_winner_mail

postcode = 'SK10 3PX'

#Init and connect to postcode homepage
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
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

driver.get("https://pickmypostcode.com/?postcode=SK10+3PX&email=george.steel92\%40gmail.com#")
sleep(2)

#Click away the fucking Cookies notice
driver.find_elements_by_css_selector("button.qc-cmp-button")[0].click()
driver.find_elements_by_css_selector("button.qc-cmp-button.qc-cmp-save-and-exit")[0].click()

#Get results of main draw
maindraw_result = driver.find_elements_by_css_selector("p.result--postcode")[0]
if postcode in maindraw_result.text:
    print("Main Draw Winner!")
    send_winner_mail(f"Won the Postcode Lottery Main Draw! {maindraw_result.text}")
    sleep(2)
    
#End session
driver.close()
exit()