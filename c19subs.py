##### Author Credit #########
#
# Christopher Liner
# Department of Geosciences
# University of Arkansas
# Fayetteville, AR
# USA
# 19 Dec 2020 (modified thru 7 May 2021)
#

import numpy as np
import pandas as pd

def getRegionXY(region,rmode,dmode):
    # region = region name as given in CSSEGIS data, for mode=1
    # rmode
    #   1 = world (region ignored)
    #   2 = country, examples 'US' 'Italy'
    #   3 = US state
    # dmode
    #   1 = get total death data
    #   2 = get total confirmed cases data
    baseURL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/"
    if rmode==1:     # world
        #print('rmode =',rmode)
        if dmode==1:
            fileName = "time_series_covid19_deaths_global.csv"
        if dmode==2:
            fileName = "time_series_covid19_confirmed_global.csv"
        df = pd.read_csv(baseURL + fileName)
        # remove / character in column name so we can search on CountryRegion
        df.columns = df.columns.str.replace('Country/Region', 'CountryRegion')
        df.drop(df.iloc[:, 0:4], inplace=True, axis=1)
        # print(df.shape)
        # df.sample(10)
        dfs1 = df.sum(axis=0)
        dfs1 = dfs1.reset_index(drop=False)
        dfs1 = dfs1.reset_index(drop=False)
        dfs1.columns = ['Timestep','index','Deaths']
        # print(dfs.shape)
        # print(dfs.head())
        dfs1.drop('index',axis=1,inplace=True)
        # make x,y numpy arrays to return
        x = np.array(dfs1['Timestep']) + 1
        y = np.array(dfs1['Deaths'])
    if rmode==2:     # country
        #print('rmode =',rmode)
        if dmode==1:
            fileName = "time_series_covid19_deaths_global.csv"
        if dmode==2:
            fileName = "time_series_covid19_confirmed_global.csv"
        df = pd.read_csv(baseURL + fileName)
        df.columns = df.columns.str.replace('Country/Region', 'CountryRegion')
        dfs2 = df[df.CountryRegion.str.contains(region,case=True)]
        dfs2.drop(dfs2.iloc[:, 0:4], inplace=True, axis=1)
        # print(df.shape)
        # df.sample(10)
        dfs2 = dfs2.sum(axis=0)
        dfs2 = dfs2.reset_index(drop=False)
        dfs2 = dfs2.reset_index(drop=False)
        dfs2.columns = ['Timestep','index','Deaths']
        # print(dfs.shape)
        # print(dfs.head())
        dfs2.drop('index',axis=1,inplace=True)
        # fit
        x = np.array(dfs2['Timestep']) + 1
        y = np.array(dfs2['Deaths'])
    if rmode==3:     # state
        #print('rmode =',rmode)
        if dmode==1:
            fileName = "time_series_covid19_deaths_US.csv"
        if dmode==2:
            fileName = "time_series_covid19_confirmed_US.csv"
        df = pd.read_csv(baseURL + fileName)
        # these are cummulative numbers
        df = df[df.Province_State.str.contains(region,case=True)]
        df.drop(df.iloc[:, 0:11], inplace=True, axis=1)
        #print(df.shape)
        dfs2 = df.sum(axis=0)
        #print(dfs.head(),dfs.tail)
        dfs2 = dfs2.reset_index(drop=False)
        dfs2 = dfs2.reset_index(drop=False)
        dfs2.columns = ['Timestep','index','Deaths']
        #print(dfs.shape)
        #print(dfs.head())
        dfs2.drop(dfs2.index[:1], inplace=True)
        dfs2.drop('index',axis=1,inplace=True)
        # fit
        x = np.array(dfs2['Timestep']) + 1
        y = np.array(dfs2['Deaths'])
    if rmode>3 or rmode<1:
        #print('rmode =',rmode)
        print('getRegionXY: Mysterious rmode value = ',rmode)
        exit()
    return x, y
