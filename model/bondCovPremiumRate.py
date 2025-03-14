# -*- coding: utf-8 -*-
# model/bondCovPremiumRate.py

from sqlalchemy import Column, Integer, String, Float, Date,  ForeignKey
from .timeModel import  TimeModel

class BondCovPremiumRate(TimeModel):
    '''
    可转债溢价率
    '''
    __tablename__ = 'bond_cov_premium_rate'
    bond_code =  Column(String(10), index=True)
    bond_id = Column(Integer, ForeignKey('bond_cov.id'), index=True)
    date = Column(Date)
    close_price = Column(Float)  #收盘价
    bond_value = Column(Float)                        #纯债价值
    conversion_value  = Column(Float)              #转股价值
    bond_premium_rate = Column(Float)           #纯债溢价率
    bond_cov_premium_rate = Column(Float)   #转股溢价率
