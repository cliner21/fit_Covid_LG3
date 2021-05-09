##### Author Credit #########
#
# Christopher Liner
# Department of Geosciences
# University of Arkansas
# Fayetteville, AR
# USA
# 19 Dec 2020 (modified thru 7 May 2021)
#
##### begin input #########
# region
region = 'India'
# region mode
#   1 = world (region ignored)
#   2 = country, examples 'US' 'Italy'
#   3 = US state
rmode = 2 
# data mode
#   1 = get total death data
#   2 = get total confirmed cases data
dmode = 1
##### end input   #########

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from datetime import datetime
from os.path import isfile
from os.path import isdir
import numpy as np
import scipy.optimize as optim
from scipy.stats import lognorm
import c19subs as cs
import time
from matplotlib.dates import MonthLocator, DateFormatter 
from matplotlib.ticker import FuncFormatter

#make a directory to save figures if it doesn't exist
figdir = "figs"
if not isdir(figdir):
    os.mkdir(figdir)
    
# define fitting functions as sum of 3 lognormals with 12 params a-l

def LG3_total(x,a,b,c,d,e,f,g,h,i,j,k,l):
    return a*lognorm.cdf(x,s=b,loc=c,scale=d)\
            +e*lognorm.cdf(x,s=f,loc=g,scale=h)\
            +i*lognorm.cdf(x,s=j,loc=k,scale=l)

def LG3_daily(x,a,b,c,d,e,f,g,h,i,j,k,l):
    return a*lognorm.pdf(x,s=b,loc=c,scale=d)\
            + e*lognorm.pdf(x,s=f,loc=g,scale=h)\
            +i*lognorm.pdf(x,s=j,loc=k,scale=l)

def fitLG3(x,y):    
    # fit the data with 3 lognormal curves
    #p0 = [100,100,100,100,100,100,100,100,100,100,100,100]
    #p0 = [1,1,1,1,1,1,1,1,1,1,1,1]
    p0 = [148342., 0.719, 56.8, 47.8, 125367., 0.868, 153., 100.2, 999999., 0.159, 3.676e-06, 418.9]
    #p0 = [100000.,1.,100.,1000.,100000.,0.1,0.01,100.,100000.,0.1,100.,100.]
    bounds = (0,[1.0e6,1.0e2,1.0e6,1.0e6,1.0e6,1.0e6,1.0e6,1.0e6,1.0e6,1.0e6,1.0e6,1.0e6])
    (a,b,c,d,e,f,g,h,i,j,k,l),pcov = optim.curve_fit(LG3_total,x,y,p0=p0,bounds=bounds,maxfev=5000)
    perr = np.sqrt(np.diag(pcov))
    return a,b,c,d,e,f,g,h,i,j,k,l,perr

# get data
x,y = cs.getRegionXY(region,rmode=rmode,dmode=dmode)
yd = np.diff(y,axis=0)
xd = x[:-1]

# set up for labeling start of each month on x axis
now = time.strftime("%Y-%m-%d")
# dates for existing data
xdates_data = np.arange("2020-01-22", now, dtype=np.datetime64)
# dates including predictions
xdates_pred = np.arange("2020-01-22", "2021-12-31", dtype=np.datetime64)

month_fmt = DateFormatter('%b')
def m_fmt(x, pos=None):
    return month_fmt(x)

# int index from 1 to end of prediction
xp = np.arange(1,len(xdates_pred)+1,1)
print(len(xdates_pred),len(xp))

# fit the observed data
a,b,c,d,e,f,g,h,i,j,k,l,perr = fitLG3(x,y)
print(a,b,c,d,e,f,g,h,i,j,k,l)

# predict in data range and beyond
y2t = LG3_total(xp,a,b,c,d,e,f,g,h,i,j,k,l)
y2d = LG3_daily(xp,a,b,c,d,e,f,g,h,i,j,k,l)

# make figure
fig, (ax1,ax2) = plt.subplots(2,1,figsize=(10,8))
# plot of total data and fit
if freeze == 0:
    ax1.plot(xdates_pred,y2t,c='r',label='model fit')
if freeze == 1:
    ax1.plot(xdates_pred,y2t,c='r',label='19 dec model fit')
ax1.scatter(xdates_data,y,s=15,alpha=0.5,label='data')
if freeze == 0:
    ax1.axvline(xdates_pred[345],linestyle="--",linewidth=2,color='gray')
if freeze == 1:
    ax1.axvline(xdates_pred[331],linestyle="--",linewidth=1,color='gray',label='19 dec 2020')
ax1.set_title(region + ' Covid-19 Deaths: Total')
ax1.xaxis.set_major_locator(MonthLocator())
ax1.xaxis.set_major_formatter(FuncFormatter(m_fmt))
ax1.grid()
ax1.text(0.98,0.05,'\ncliner '+datetime.now().strftime('%d %b %Y'), \
          fontsize=7, horizontalalignment='right',\
          bbox=dict(facecolor='w', edgecolor='w', alpha=0.5),\
          transform = ax1.transAxes)
ax1.legend(loc='upper left')
# plot of daily data and fit
if freeze == 0:
    ax2.plot(xdates_pred,y2d,c='r',label='model fit')
if freeze == 1:
    ax2.plot(xdates_pred,y2d,c='r',label='19 dec model fit')
ax2.scatter(xdates_data[:-1],yd,s=15,alpha=0.5,label='data')
if freeze == 0:
    ax2.axvline(xdates_pred[345],linestyle="--",linewidth=2,color='gray')
if freeze == 1:
    ax2.axvline(xdates_pred[331],linestyle="--",linewidth=1,color='gray',label='19 dec 2020')
ax2.set_title(region + ' Covid-19 Deaths: Daily')
ax2.xaxis.set_major_locator(MonthLocator())
ax2.xaxis.set_major_formatter(FuncFormatter(m_fmt))
ax2.grid()
ax2.text(0.98,0.05,'\ncliner '+datetime.now().strftime('%d %b %Y'), \
          fontsize=7, horizontalalignment='right',\
          bbox=dict(facecolor='w', edgecolor='w', alpha=0.5),\
          transform = ax2.transAxes)
ax2.legend(loc='upper left')

fig.tight_layout(pad=2, h_pad=2.5)

s = figdir + '/' + 'LG3_' + datetime.now().strftime('%b%d') + '_'+region
plt.savefig(s+ '.pdf')
plt.savefig(s+ '.png',dpi=600)

#plt.show()