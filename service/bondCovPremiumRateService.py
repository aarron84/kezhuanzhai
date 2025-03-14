# -*- coding: utf-8 -*-
# service/bondCovPremiumRateService.py

from model import BondCovPremiumRate,  BondCov
from database import Database
import akshare as ak
from utils import exception_handle
import time,  math

class BondCovPremiumRateService:
    '''
    可转债溢价率
    '''
    def __init__(self, session):
        self.session = session
        self.bondCovPremiumRate_dal = Database(session, BondCovPremiumRate)
        self.bondCov_dal = Database(session,  BondCov)
    @exception_handle
    def getPremiumRatesFromOther(self, bond: BondCov):
        bond_zh_cov_value_analysis_df = ak.bond_zh_cov_value_analysis(symbol=bond.bond_code)
        premiumRates = []
        for row in bond_zh_cov_value_analysis_df.itertuples():
            p = BondCovPremiumRate()
            p.bond_code = bond.bond_code
            p.bond_id = bond.id, 
            p.date = row.日期
            p.close_price = None if math.isnan(row.收盘价) else row.收盘价         
            p.bond_value= None if math.isnan(row.纯债价值) else row.纯债价值 
            
            p.conversion_value = None if math.isnan(row.转股价值) else row.转股价值
            p.bond_premium_rate =None if math.isnan(row.纯债溢价率) else row.纯债溢价率
            p.bond_cov_premium_rate = None if math.isnan(row.转股溢价率) else row.转股溢价率
            premiumRates.append(p)
        return premiumRates
            
    @exception_handle
    def collectPremiumRates(self):
        '''
        采集溢价率
        '''
        bonds = self.bondCov_dal.get_all()
        for bond in bonds:
            list = self.getPremiumRatesFromOther(bond)
            lastDate = self.bondCovPremiumRate_dal.getMax(BondCovPremiumRate.date, BondCovPremiumRate.bond_code == bond.bond_code)
            noExists= list if list is not None else  []
            if lastDate is not None:
                noExists = [ item for item in list if item.date > lastDate ]
            self.bondCovPremiumRate_dal.bulk_add(noExists)
            time.sleep(1.5)
            
        
