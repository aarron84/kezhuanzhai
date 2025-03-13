# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Float, Date
import enum
from .timeModel import  TimeModel



class BondCovStatus(enum.Enum):
    UNLIST = -1
    LIST = 0
    DELIST = 1

class BondCov(TimeModel):
    __tablename__ = 'bond_cov'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bond_code = Column(String(10), unique=True, index=True)
    name = Column(String(10))
    stock_code = Column(String(10), index=True)
    stock_name = Column(String(10))
    conversion_price = Column(Float,  nullable=True)   #转换价格
    issue_size = Column(Float)  # 发行规模
    list_date = Column(Date)    # 上市日期
    credit_rating = Column(String(10)) # 信用评级
    maturity_date = Column(Date) # 到期日
    status = Column(Integer,  default=BondCovStatus.LIST.value) #状态
    final_trading_date = Column(Date)     #最后交易日期
    put_size = Column(Float)                  #回售规模
    left_size = Column(Float)                  #剩余规模
    listed_years = Column(Float)               #存续年限
    last_price = Column(Float)                  #最后交易价格
    low_price = Column(Float)                 #最低价格
    low_price_date = Column(Date)
    high_price = Column(Float)                  #最高价格
    high_price_date = Column(Date)
    delisted_note = Column(String(20))    #退市原因



