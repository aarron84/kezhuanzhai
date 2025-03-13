# -*- coding: utf-8 -*-
# task/JisiBondDelistedTask.py

from database import Database,  DatabaseSession
import  jisilu as js
class JisiBondDelisted:
    def run(self):
        bonds = js.bond_deListed_jsl()
    with DatabaseSession.get_session() as session:   
   
        bondCov_dal = Database(session, BondCov)        
        for bond in bonds:            
            bondCov_dal.update(BondCov.bond_code == bond.bond_code,
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
