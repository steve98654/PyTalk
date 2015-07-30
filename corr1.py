import pandas as pd 
import datetime as dt
import matplotlib.pyplot as plt 

df = pd.read_csv('all_stocks.csv')
df['Date'] = pd.to_datetime(df['Date'],format='%Y-%d-%m')  # convert to datetime 

# Make a single dataframe of open prices    

tkrs = sorted(list(set(df['Symbol'])))
fdf = pd.DataFrame()

for j in xrange(0,len(tkrs)):
    tmpdate = df[df.Symbol==tkrs[j]]['Date']
    tmpopen=df[df.Symbol==tkrs[j]]['Open']
    tmpdf=pd.DataFrame(tmpopen.values, index=tmpdate.values, columns=[tkrs[j]])
    fdf = pd.concat([fdf,tmpdf], axis=1)

fdf.to_pickle('home/steve98654/Desktop/PyTalk/open_price.pkl')

