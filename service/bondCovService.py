# -*- coding: utf-8 -*-
# bondCovService.py
import akshare as ak
from model import BondCov
from database import Database, DatabaseSession
import math
from typing import  List,  Optional
class BondCovService:
    
    def __init__(self,  session):        
        self.session = session
        self.bondCov_dal = Database(self.session, BondCov)
    
    '''
    从其它地方获取所有可转债数据一览表
    '''
    def  getListFromOther(self):         
        bond_zh_cov_df = ak.bond_zh_cov()
        bonds = [];
        for index , row in bond_zh_cov_df.iterrows():
           bond = BondCov(bond_code = row['债券代码'], name=row['债券简称'])
           bond.stock_code = row['正股代码']
           bond.stock_name = row['正股简称']
           bond.issue_size = row['发行规模']       
           bond.conversion_price = row['转股价']
           bond.conversion_price = None if math.isnan(bond.conversion_price) else bond.conversion_price
           bond.list_date = row['上市时间']
           bond.credit_rating = row['信用评级']
           bonds.append(bond)        
        return bonds
    '''
    从其它地方获取所有可转债数据一览表并保存
    '''    
    def getListAndSaveFromOther(self):
        list = self.getListFromOther()
        self.bondCov_dal.bulk_add(BondCov, list)
        return list
        
    def getAll(self,  filter) ->List[BondCov]:
        return self.bondCov_dal.get_all(filter)
