import pandas as pd 
import datetime as dt
from pandas.io.data import DataReader 

tickerdf = pd.read_csv('SandP500_wiki.csv')    # read in S&P 500 tickers 
tickers = tickerdf['Ticker symbol']       # extract list of tickers from dataframe
verbose_flag = False                      # flag that turns on ticker print statements
start_date = dt.datetime(2010, 1, 1)      # date when to start downloading data
ticker_df_list = []                       # initialize list of dataframes for each ticker                          

for ticker in tickers: 
    try:
        r = DataReader(ticker, "google", start=start_date)   # download price data from yahoo 
        r['Ticker'] = ticker 
        ticker_df_list.append(r)
        if verbose_flag:
            print "Obtained data for ticker %s" % ticker  
    except:
        if verbose_flag:
            print "No data for ticker %s" % ticker  

df = pd.concat(ticker_df_list)            # build single df of all data
cell= df[['Ticker','Close']]          # extract ticker and close price information 
cell.reset_index().sort(['Ticker', 'Date'], ascending=[1,0]).set_index('Ticker')
cell.to_pickle('google_close_price.pkl')         # pickle data
