# -*- coding: utf-8 -*-
# service/BondCovDailyService.py
import akshare as ak
from model import BondCovDaily, BondCov, BondCovStatus
from database import Database
from utils import StockExchange,  appLogger
from utils import exception_handle

class  BondCovDailyService:
    
    def __init__(self,  session):        
        self.session = session
        self.bondCovDaily_dal = Database(self.session, BondCovDaily)
        self.bondCov_dal = Database(self.session, BondCov)
    @exception_handle
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
        
    def get(self,  *where):
        return self.bondCovDaily_dal.get(*where)
    
    @exception_handle
    def collectBondCovDaily(self, bondCov: BondCov):       
        list = self.getListFromOther(bondCov)  
        lastDate = self.bondCovDaily_dal.getMax(BondCovDaily.date)
        notExists = [ item for item in  list if item.date >lastDate]
        self.bondCovDaily_dal.bulk_add(notExists)
    
    
    def getMax(self,  column,  *where):
        return self.bondCovDaily_dal.getMax(column,   *where)
        
    @exception_handle
    def collectAllBondCovDaily(self):    
        bonds = self.bondCov_dal.get_all(BondCov.status == BondCovStatus.LIST.value)      
        for bond in bonds:    
            list = self.getListFromOther(bond)             
            if list is None:
                appLogger.error(f"获取{bond.name}, {bond.bond_code}的日历史行情失败")
                continue
            lastDate = self.bondCovDaily_dal.getMax(BondCovDaily.date,  BondCovDaily.bond_code == bond.bond_code)
     
            notExists = [ item for item in  list if item.date >lastDate]
            self.bondCovDaily_dal.bulk_add(notExists)
    @exception_handle 
    def test(self):
        bonds = self.bondCov_dal.get_all(BondCov.status == BondCovStatus.LIST.value)      
        for bond in bonds:    
            list = self.getListFromOther(bond)             
            if list is None:
                appLogger.error(f"获取{bond.name}, {bond.bond_code}的日历史行情失败")
                continue
            lastDate = self.bondCovDaily_dal.getMax(BondCovDaily.date,  BondCovDaily.bond_code == bond.bond_code)
     
            
    
