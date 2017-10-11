# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:56:27 2017

@author: George
"""

import pandas as pd
import numpy as np
from matplotlib.finance import candlestick2_ochl
import matplotlib.pyplot as plt
from talib import STOCH

path='EURUSD.csv'
base='G:/#quant data/real/'
#path='hs300_1h.csv'
#base='G:/#quant data/ch/1h/'
d=pd.read_csv(base+path,index_col='Date Time')
d.index=pd.to_datetime(d.index)
l=200
f=d[-l:]

opens=f['Open']
closes=f['Close']
highs=f['High']
lows=f['Low']

k,d=STOCH(f.High.values, f.Low.values, f.Close.values, fastk_period=8, slowk_period=3,
          slowk_matype=0, slowd_period=3, slowd_matype=0)

fig=plt.figure(figsize=(11,8))
ax1=fig.add_subplot(2,1,1)
candlestick2_ochl(ax1,opens,closes,highs,lows,width=0.5,colorup='r',colordown='g')
ax1.set_xticks(np.linspace(0,l-1,6).astype('int'))
ax1.set_xticklabels(f.index[np.linspace(0,l-1,6).astype('int')])
ax1.grid(color='r', linestyle='--', linewidth=1)

ax2=fig.add_subplot(2,1,2)
ax2.plot(k)
ax2.plot(d)
ax2.set_xticks(np.linspace(0,l-1,6).astype('int'))
ax2.set_yticks([15,20,30,40,50,60,70,80,85])
ax2.set_xticklabels(f.index[np.linspace(0,l-1,6).astype('int')])
ax2.grid(color='b', linestyle='--', linewidth=1)
plt.show()