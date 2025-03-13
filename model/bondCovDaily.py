# -*- coding: utf-8 -*-
# model/bondCovDaily.py
from sqlalchemy import Column, Integer, String, Float, Date,  ForeignKey
from .timeModel import  TimeModel

class BondCovDaily(TimeModel):
    __tablename__ = 'bond_cov_daily'
    id = Column(Integer, primary_key=True, autoincrement=True,)
    bond_code =  Column(String(10), index=True)
    bond_id = Column(Integer, ForeignKey('bond_cov.id'), index=True)
    date =Column(Date)   #日期
    open = Column(Float) #开盘价
    high  = Column(Float)  #最高价
    low = Column(Float) #最低价
    close = Column(Float)  #收盘价
    volume = Column(Float) #交易量或金额

    def keys(self):
        return ('id', 'bond_code','bond_id','date', "open", "high", "low", "close", 'volume')
    
    def __getitem__(self, item):        
        return getattr(self, item)
