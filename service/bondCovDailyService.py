# -*- coding: utf-8 -*-
# service/BondCovDailyService.py
import akshare as ak
from model import BondCovDaily, BondCov
from database import Database
from utils import StockExchange
import traceback

class  BondCovDailyService:
    
    def __init__(self,  session):        
        self.session = session
        self.bondCovDaily_dal = Database(self.session, BondCovDaily)
        
    def  getListFromOther(self, bondCov: BondCov):
        bond_code = StockExchange.get_bondCodeWithStockExchange(bondCov.bond_code)
        bond_zh_hs_cov_daily = ak.bond_zh_hs_cov_daily(symbol=bond_code)
        bond_dailys = []
        for index , row in bond_zh_hs_cov_daily.iterrows():
           bond = BondCovDaily(bond_code = bondCov.bond_code, bond_id=bondCov.id)
           
           bond.date = row['date']
           bond.open = row['open']
           bond.high = row['high']       
           bond.low = row['low']
           bond.close = row['close']   
           bond.volume = row['volume']
           bond_dailys.append(bond)        
        return bond_dailys
    
    def getListAndSaveFromOther(self, bondCov: BondCov):
        try:
            list = self.getListFromOther(bondCov)      
            self.bondCovDaily_dal.bulk_add(list)
        except Exception as ex:            
            print(f"bond_code={bondCov.bond_code},An error occurred:", ex)
            print("Traceback:")
            traceback.print_exc()
            
            
    
