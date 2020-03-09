from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import imaplib
import base64
import re
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

#Load Firefox profile
profile = webdriver.FirefoxProfile("C:/Users/georg/AppData/Roaming/Mozilla/Firefox/Profiles/ul5p82rs.default-release")
driver = webdriver.Firefox(firefox_profile=profile,
                           executable_path="C:/Bots/bin/geckodriver.exe",
                           log_path='C:/Bots/logs/gmail.log')


def readMessage(content)->str:
    message = None
    if "data" in content['payload']['body']:
        message = content['payload']['body']['data']
        message = data_encoder(message)
    elif "data" in content['payload']['parts'][0]['body']:
        message = content['payload']['parts'][0]['body']['data']
        message = data_encoder(message)
    else:
        print("body has no data.")
    return message

def data_encoder(text):
    if len(text)>0:
        message = base64.urlsafe_b64decode(text)
        message = str(message, 'utf-8')
        #message = email.message_from_string(message)
    return message
  
def FindUrl(string): 
    # findall() has been used  
    # with valid conditions for urls in string 
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string) 
    return url 



# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

"""Shows basic usage of the Gmail API.
Lists the user's Gmail labels.
"""
creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('gmail', 'v1', credentials=creds)

# Call the Gmail API
results = service.users().messages().list(userId="me",
                                          prettyPrint=True,
                                          q="from: noreply@ebesucher.de",
                                          maxResults=10).execute()

for mail in results["messages"]:
    msg = service.users().messages().get(id=mail["id"],
                                   userId="me",
                                   format="full",
                                   prettyPrint=True).execute()
    
    if "UNREAD" in msg["labelIds"]:
        print(msg["snippet"])
        body = readMessage(msg)
        if "So that you will be reimbursed, you have to read the email." in body:
            links = FindUrl(body)
            for link in links:
                if "showmail" in link:
                    print("We did it!")
                    sleep(2)
                    driver.get(link)
                    sleep(35)
                    break

driver.quit()
exit()
