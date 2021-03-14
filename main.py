# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:01:23 2021

@author: 46362
"""
import pandas as pd
import numpy as np
file = r"C:\Users\46362\Desktop\home\高频交易论文\IF00\2015"

def cal_trade_direction(data,method='tick'):
    if method=='tick':
        direction=np.diff(data['price']).tolist()
        direction.insert(0,1)
        direction=np.array(direction)
            
        direction=np.where(direction>0,1,np.where(direction==0,0,-1))
        direction=pd.Series(direction)
        while (direction==0).sum()>0:
            mask=direction.index[direction==0]
            direction[mask]=direction[mask-1]
        data['direction']=direction
            
    if method=='LR':
        quote=(data.buy1+data.sale1)/2
        direction=np.where(data.price>quote,1,np.where(data.price==quote,0,-1))
        direction[0]=1
        direction=pd.Series(direction)
        while (direction==0).sum()>0:
            mask=direction.index[direction==0]
            direction[mask]=direction[mask-1]
            data['direction']=direction
    return data

def process_data(df):  
    data = df[['price', 'buy_vol', 'sale_vol','buy1','sale1','bc1','sc1']]
    data['vol'] = data.buy_vol+data.sale_vol
    data['isBuy'] = (data.buy_vol-data.sale_vol>0)
    data['time'] = pd.to_datetime(df.time)
    data['order_imbalance']=data['bc1']-data['sc1']
    data['order_imbalance']=abs(data.order_imbalance.diff().fillna(0))
    
    data=cal_trade_direction(data)    
    
    y,m,d = data.time.iloc[0].year, data.time.iloc[0].month, data.time.iloc[0].day
    start_time = pd.to_datetime(str(y)+'-'+str(m)+'-'+str(d)+' 9:30:00')
    end_time = pd.to_datetime(str(y)+'-'+str(m)+'-'+str(d)+' 15:00:00')
    data = data[(data.time>=start_time) & (end_time>=data.time)]
    #morning_end_time = pd.to_datetime(str(y)+'-'+str(m)+'-'+str(d)+' 11:30:00')
    #afternoon_start_time = pd.to_datetime(str(y)+'-'+str(m)+'-'+str(d)+' 13:00:00')
    #data = data[(data.time<=morning_end_time) | (data.time>=afternoon_start_time)]
    data = data.set_index('time')
    #return [data,morning_end_time,afternoon_start_time]
    return data

def main(path):  
    f=open(file)
    df = pd.read_csv(f, index_col=False)
    data=process_data(df)
    return data
       