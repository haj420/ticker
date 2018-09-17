#!/usr/bin/env python
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
plt.use('GTKAgg')
import matplotlib.ticker as mticker
import matplotlib.dates as mdates

eachStock = 'TSLA', 'AAPL'

def graphData(stock):
     try:
	stockfile = stock+'.txt'

	date, closep, highp, lowp, openp, volume = np.loadtxt(stockFile, delimiter=',',unpack=True,converters={ 0: smdates.strpdate2num('%Y%m%d')})

	fig = plt.figure()
	ax1 = plt.subplot(1,1,1)
	ax1.plot(date, openp)
	ax1.plot(date, highp)
	ax1.plot(date, lowp)
	ax1.plot(date, closep)
 	
	plt.show()

     except Exception, e:
	print 'failed main loop',str(e)

for stock in eachStock:
	graphData(stock)
	time.sleep(555)
