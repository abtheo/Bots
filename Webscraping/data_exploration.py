import pandas as pd
import matplotlib
import emoji 
import matplotlib.pyplot as plt
  
history = pd.read_csv("emoji_history.csv")

emoji_set = set()
for i in range(1,6):
    emoji_set.update(set(history[f"value{i}"].values))

all_emojis = dict(zip(list(emoji_set), range(len(emoji_set))))

def to_class(x):
    try:
        return all_emojis[x]
    except:
        return x

class_df = history.applymap(lambda x: to_class(x))

print(class_df.head())

from collections import Counter


total_counts = Counter()
for i in range(1,6):
    total_counts += Counter(class_df[f"value{i}"])

"""Print most common"""
# for k,t in total_counts.most_common():
#     print(u'\\'+ list(all_emojis.keys())[list(all_emojis.values()).index(k)])


"""Write frequencies to HTML file"""
# import os
# with open('test.html','w',encoding='utf-8-sig') as f:
#     f.write('<meta charset="utf-8">')
#     for k,t in total_counts.most_common():
#         #out = list(all_emojis.keys())[list(all_emojis.values()).index(k)].decode('unicode-escape')
#         out = (list(all_emojis.keys())[list(all_emojis.values()).index(k)]) + "\r\n :" + str(t)
#         f.write(out)
#         f.write("<br />")
# os.startfile('test.html')    

"""Plot frequencies histogram"""
# class_df.hist(bins=len(all_emojis))
# plt.show()