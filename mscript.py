## Main Download and Format Data Script

import datetime
import pandas as pd
from pandas import DataFrame
from pandas.io.data import DataReader

# Build up a potential list of stock names 
# We got the NASDAQ, NYSE, and AMEX lists from: 
# http://www.nasdaq.com/screening/company-list.aspx

# list of s and p 500 companies and tickers 
# http://data.okfn.org/data/core/s-and-p-500-companies/r/constituents.csv

tickerdf = pd.read_csv('SandP500.csv')
tickers = list(symboldf['Symbol'].values)
symbols = []

for ticker in tickers: 
    try:
        r = DataReader(ticker, "yahoo", start=datetime.datetime(2010, 01, 01))
        r['Symbol'] = ticker 
        symbols.append(r)
        print "Obtained data for ticker %s" % ticker  
    except: 
        print "No data for ticker %s" % ticker  

df = pd.concat(symbols)
cell= df[['Symbol','Adj Close']]
cell.reset_index().sort(['Symbol', 'Date'], ascending=[1,0]).set_index('Symbol')
cell.to_pickle('close_price.pkl')

####### Begin contents of corr1.py

#df = pd.read_csv('all_stocks.csv')
#df['Date'] = pd.to_datetime(df['Date'],format='%d/%m/%Y')  # convert to datetime 

# Make a single dataframe of open prices    

#tkrs = sorted(list(set(df['Symbol'])))
#fdf = pd.DataFrame()

#for j in xrange(2310,len(tkrs)):
#    tmpdate = df[df.Symbol==tkrs[j]]['Date']
#    tmpopen=df[df.Symbol==tkrs[j]]['Open']
#    tmpdf=pd.DataFrame(tmpopen.values, index=tmpdate.values, columns=[tkrs[j]])
#    fdf = pd.concat([fdf,tmpdf], axis=1)
#
#fdf.to_pickle('open_price.pkl')

