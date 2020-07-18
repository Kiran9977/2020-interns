import urllib.request as request
import json
import pandas as pd
import matplotlib.pyplot as plt
import datetime

d=False
while not d:
        try:
                date_entry = input('Enter a start date from data u want date in YYYY-MM-DD format:')
                year, month, day = map(int, date_entry.split('-'))
                Sdate = datetime.date(year, month, day)

                date_entry2 = input('Enter a end date upto data u want date in YYYY-MM-DD format:')
                year1, month1, day1 = map(int, date_entry2.split('-'))
                Edate = datetime.date(year1, month1, day1)
                d=True

        except:
                print("wrong entry")


isValid=False
while not isValid:
	a=input("enter valid symbol:")
	try:
                with request.urlopen('https://api.exchangeratesapi.io/history?start_at={1}&end_at={2}&symbols={0}'.format(a,Sdate,Edate)) as response:

                    source = response.read()
                    data1 = json.loads(source)
                    isValid=True
	except:
		        print ("try again!\n")


df=pd.DataFrame(data1['rates'])

x=[]
date=[]

for row in df:
	date.append(row)

df1=df.transpose()

x=df1[a].tolist()

plt.plot(date,x, label=a)
plt.ylabel('Y')
plt.xlabel('date')
plt.title('Exchange Rate Against EUR')
plt.legend()
plt.show()
