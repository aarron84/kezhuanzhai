# -*- coding: utf-8 -*-
# service/bondCovDeListed.py
import sys

from model import   BondCov, BondCovStatus
from database import  Database
import jisilu as js
from utils import exception_handle
import time
class BondCovDelistedService:
    def __init__(self,  session):  
        self.session = session
        self.bondCov_dal =Database(session,  BondCov)
    
    @exception_handle
    def collectDelisted(self):
        bonds = js.bond_deListed_jsl()
        for bond in bonds:            
            self.bondCov_dal .update(BondCov.bond_code == bond.bond_code ,  BondCov.status == BondCovStatus.LIST,
            last_price=bond.last_price, 
            final_trading_date = bond.final_trading_date, 
            low_price = bond.low_price, 
            low_price_date = bond.low_price_date, 
            high_price = bond.high_price, 
            high_price_date = bond.high_price_date, 
            left_size = bond.left_size, 
            put_size = bond.put_size, 
            isDelisted = bond.isDelisted, 
            listed_years = bond.listed_years, 
            delisted_note = bond.delisted_note       
            ) 
