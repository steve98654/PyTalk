import pandas as pd 
import datetime as dt
import matplotlib.pyplot as plt 
from scipy.stats import mode 
from scipy.stats.stats import pearsonr
import numpy as np 
import numpy.linalg as LA 
import scipy.cluster.hierarchy as sch
import seaborn as sns
from nearest_correlation import nearcorr

def eigden(lam,t,m):
    q = float(t)/float(m)
    lplus = (1+1/q+2*np.sqrt(1/q))
    lminus = (1+1/q-2*np.sqrt(1/q))
    return q/(2*np.pi*lam)*np.sqrt((lplus-lam)*(lam-lminus))

def lamplus(t,m): 
    q = float(t)/float(m)
    return (1+1/q+2*np.sqrt(1/q))

dte1 = '2010-07-01'
dte2 = '2015-07-01'

df = pd.read_pickle('close_price.pkl')
tickers = sorted(list(set(df['Symbol'].values)))
tkrlens = [len(df[df.Symbol==tkr][dte1:dte2]) for tkr in tickers]
tkrmode = mode(tkrlens)[0][0]

good_tickers = [tickers[i] for i,tkr in enumerate(tkrlens) if tkrlens[i]==tkrmode]

rtndf = pd.DataFrame()
for tkr in good_tickers: 
    tmpdf = df[df.Symbol==tkr]['Adj Close'][dte1:dte2]
    tmprtndf = ((tmpdf-tmpdf.shift(1))/tmpdf).dropna()
    rsdf = tmprtndf/tmprtndf.std()
    rtndf = pd.concat([rtndf, rsdf],axis=1)

rtndf = rtndf.dropna()
rtndf.columns = good_tickers

t,m = rtndf.shape
cmat = rtndf.corr()

evls, evcs = LA.eig(cmat)
rcmat = abs(np.dot(np.dot(evcs,np.diag(evls)),LA.inv(evcs)))
evallst = map(abs,evls)

filtvals = [val for val in evallst if val < lamplus(t,m)]
sevlist = [np.mean(filtvals)]*len(filtvals)
feval = evallst[:(len(evallst)-len(sevlist))] + sevlist

rcmat = abs(np.dot(np.dot(evcs,np.diag(feval)),LA.inv(evcs)))
rcmat = (rcmat + rcmat.T)/2
ncorr = nearcorr(rcmat, max_iterations=1000) 

ncorrdf = pd.DataFrame(ncorr,columns=good_tickers,index=good_tickers)

# Start the clustering 

sns.clustermap(ncorrdf)
plt.show()


