import requests
import time
import pandas as pd
from datetime import datetime

from com.fintech.strategy.stg01.download.get_data_mine import get_intra_day
from com.fintech.strategy.stg01.download.insert_pre_open_data_mine import insert_portfolio

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print('Started process',current_time)

url = "https://www.nseindia.com/api/market-data-pre-open?key=NIFTY"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}

with requests.session() as s:
    s.get('https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market', headers=headers) #This is to attach a session in y case i needed session to call API that is why this line was added
    data = s.get(url, headers=headers).json() #You can directly put Rest API in URL and get the data in json format

df = pd.json_normalize(data['data'])
#print(df.loc[1,:])
pre_open_data=[]

for index, row in df.iterrows():
    row_data=[]
    row_data.append(row["metadata.symbol"])
    row_data.append(row["metadata.identifier"])
    row_data.append(row["metadata.lastPrice"])
    row_data.append(row["metadata.change"])
    row_data.append(row["metadata.pChange"])
    row_data.append(row["metadata.previousClose"])
    row_data.append(datetime.strptime(row["detail.preOpenMarket.lastUpdateTime"],'%d-%b-%Y %H:%M:%S'))
    pre_open_data.append(row_data)

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print('Download complete and started persisting', current_time)

insert_portfolio(pre_open_data)

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print('Completed persisting', current_time)

