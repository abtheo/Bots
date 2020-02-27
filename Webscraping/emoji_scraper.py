import requests 
from bs4 import BeautifulSoup 
import csv

entries=[]  # a list to store quotes 
  
#Loop all history pages
for n in range(1,88):
    print(f"Querying Page: {n}")
    URL = f"https://freemojilottery.com/history/page/{n}"
    r = requests.get(URL)   
    soup = BeautifulSoup(r.content, 'html5lib') 

    table = soup.find_all('tr') 
    for i,row in enumerate(table):
        if i == 0:
            continue
        #Filter date
        date = row.find("td", {"class": "draw-date"}).span.get_text()

        #Filter emoji winners
        emojis = row.findAll("object", {"class": "emojione"})
        row_emojis = str([emo['standby'].encode('unicode-escape') for emo in emojis])
        
        #Retain parsed row
        entry = {}
        entry['timestamp'] = date
        entry['value'] = row_emojis
        entries.append(entry)

#Save to output file
filename = 'emoji_history.csv'
with open(filename, 'w') as f: 
    w = csv.DictWriter(f,['timestamp','value']) 
    w.writeheader()
    for e in entries: 
        w.writerow(e)