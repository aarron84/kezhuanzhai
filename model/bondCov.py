# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey
from database import Database, BaseModel



class BondCov(BaseModel):
    __tablename__ = 'bond_cov'
    id = Column(Integer, primary_key=True, autoincrement=True,)
    bond_code = Column(String(10), unique=True, index=True)
    name = Column(String(10))
    stock_code = Column(String(10), index=True)
    stock_name = Column(String(10))
    conversion_price = Column(Float,  nullable=True)
    issue_size = Column(Float)  # 发行规模
    list_date = Column(Date)    # 上市日期
    credit_rating = Column(String(10)) # 信用评级
    maturity_date = Column(Date) # 到期日
    isDelisted = Column(Boolean,  default=False) #是否已退市
    
    def keys(self):
        return ("id", "bond_code", "name", "stock_code", 'stock_name', 'conversion_price', 'issue_size', 'list_date', 'credit_rating', 'maturity_date', 'isDelisted')
    
    def __getitem__(self, item):        
        return getattr(self, item)

