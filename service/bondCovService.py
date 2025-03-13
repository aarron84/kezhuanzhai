# -*- coding: utf-8 -*-
# bondCovService.py
import akshare as ak
from model import BondCov, BondCovStatus
from database import Database
import math
from typing import  List,  Optional
from utils import  appLogger
import pandas as pd



class BondCovService:
    
    def __init__(self,  session):        
        self.session = session
        self.bondCov_dal = Database(self.session, BondCov)
    
    '''
    从同化顺获取所有可转债数据一览表
    '''
    def  getListFromOtherThs(self) -> list[BondCov]:         
        bond_zh_cov_df = ak.bond_zh_cov_info_ths()
        bonds = [];
        
        for index , row in bond_zh_cov_df.iterrows():
           bond = BondCov(bond_code = row['债券代码'], name=row['债券简称'])
           bond.stock_code = row['正股代码']
           bond.stock_name = row['正股简称']
           bond.issue_size =  row['实际发行量']
           if bond.issue_size <=0:
               bond.issue_size = row['计划发行量']
           bond.conversion_price = row['转股价格']
           bond.conversion_price = None if math.isnan(bond.conversion_price) else bond.conversion_price
           bond.list_date = row['上市日期']
           bond.maturity_date = row['到期时间']
           if pd.isna(bond.list_date):
               bond.status = BondCovStatus.UNLIST.value
           bonds.append(bond)        
        return bonds
    '''
    从其它地方获取所有可转债数据一览表
    '''
    def  getListFromOther(self) -> list[BondCov]:         
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
           if pd.isna(bond.list_date):
               bond.list_date = None
               bond.status = BondCovStatus.UNLIST.value
           bonds.append(bond)        
        return bonds
    
    
    def collectBondCov(self) -> list[BondCov]:
        '''
    从其它地方获取所有可转债数据一览表并保存
    '''    
        list = self.getListFromOther()
        lastListDate = self.bondCov_dal.getMax(BondCov.list_date)        
        noExists = []
        for item in list: 
            if item.bond_code is None or  ((item.list_date is  not None)and item.list_date <= lastListDate):
                continue
            #待上市
            if item.list_date is None and not self.bondCov_dal.exists(BondCov.bond_code == item.bond_code):
                noExists.append(item)
                #已上市但系统中没有这条可转债记录
            elif  item.list_date is not None:                
                noExists.append(item)
        self.bondCov_dal.bulk_add(noExists)
        return list
        
    def getAll(self,  *where) ->List[BondCov]:
        return self.bondCov_dal.get_all(*where)

    def updateMaturityDate(self):
        bonds = self.getListFromOtherThs()   
        for bond in bonds:            
            self.bondCov_dal.update(BondCov.bond_code == bond.bond_code ,  BondCov.maturity_date == None,
            maturity_date=bond.maturity_date                 
            ) 
            
