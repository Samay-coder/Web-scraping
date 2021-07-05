import csv
import pandas

# df = pandas.read_csv('ScrapeDataEdited.csv')
# # df.head()
# df.drop(['Unnamed'],axis = 1,inplace = True)
# df.reset_index(drop = True,inplace = True)
# # df = df.dropna()

# # df['mass'] = df['mass'].apply(lambda x:x.replace('$','').replace(',','')).astype('float')

# # df['radius'] = float(df['radius'] * 0.102763)
# # df['mass'] = float(df['mass'] * 0.000954588)
# # df.head()

# df.to_csv('ScrapeDataEdited.csv')

data1 = []
data2 = []

with open("ScrapeData.csv",'r') as f:
    cr = csv.reader(f)
    for i in cr:
        data1.append(i)

headers1 = data1[0]
starData1 = data1[1:]

with open("ScrapeDataEdited.csv",'r') as f:
    cr = csv.reader(f)
    for i in cr:
        data2.append(i)

headers2 = data2[0]
starData2 = data2[1:]

headers = headers1 + headers2
starData = []

for i,data in enumerate(starData1):
    starData.append(starData1[i] + starData2[i])
    
with open("ScrapeDataMerged.csv",'w') as f:
    cw = csv.writer(f)
    cw.writerow(headers)
    cw.writerows(starData)