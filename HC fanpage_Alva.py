import csv
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.pyplot as figure 
import time 
from datetime import datetime 
import matplotlib.dates as md
from matplotlib.pyplot import figure

Time = []
Volume = []
with open('/Users/mumuanan/Desktop/HC增長數據.csv') as f:
    HC = csv.reader(f)
    headers=next(HC) #不去跑最上面兩row
    for row in HC:
        # print(row)
        date=row[0]  #row[0]是日期的部分
        like=int(row[1]) #row[1]是粉專按讚的部分
        Time.append(date)
        Volume.append(like)
        
figure(num=None, figsize=(18, 12), dpi=100, facecolor='w', edgecolor='k')
plt.xticks(rotation=60)
plt.xlabel("Date")
plt.ylabel("Likes")
plt.title("HC fanspage")
plt.plot(Time, Volume,"-o")
plt.show()


