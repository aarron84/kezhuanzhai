# -*- coding: utf-8 -*-
# jisilu/bondDelisted.py
import requests
from model import  BondCov,  BondCovStatus,  BondCovLeftSize
from datetime import  datetime
from utils  import  appLogger  as logger

def bond_deListed_jsl() ->list[BondCov]:
    """
    集思录已退市可转债
    :return: 集思录已退市可转债
    :rtype: List[BondCov]
    """
    url = "https://www.jisilu.cn/webapi/cb/delisted/"    
   

    try:
        r = requests.get(url) 
        data_json = r.json()
     
        datas = data_json["data"]        
        bonds = []     
        for data in datas:
            bond = BondCov(bond_code = data['bond_id'])
            bond.name = data['bond_nm']
            bond.stock_code = data['stock_id']
            bond.stock_name = data['stock_nm']        
            bond.issue_size = data['orig_iss_amt']
            bond.put_size = data['put_iss_amt']
            bond.left_size = data['curr_iss_amt']
            bond.listed_years = data['listed_years']
            bond.last_price = data['price']
            bond.low_price  = data['min_price']
            bond.low_price_date = datetime.strptime(data['min_dt'], '%Y-%m-%d') 
            bond.high_price = data['max_price']
            bond.high_price_date = datetime.strptime(data['max_dt'], '%Y-%m-%d') 
            bond.final_trading_date = datetime.strptime(data['delist_dt'], '%Y-%m-%d') 
            bond.delisted_note = data['delist_notes']
            bond.status = BondCovStatus.DELIST
            bonds.append(bond)
        return  bonds
        
    except Exception as e:
        logger.exception(e)
        return []
        
def bond_left_size(bond_code: str) -> list[BondCovLeftSize]:
    '''
    获取可转债剩余规模历史记录
    '''
    url = f"https://www.jisilu.cn/data/cbnew/detail_pic/?display=curr_iss_amt&bond_id={bond_code}"  
    leftSizes = []
    try:
        r = requests.get(url) 
        data_json = r.json()       
        if "picdata" in data_json:
            picdata = data_json["picdata"]         
            for data in picdata:
                bondCovLeftSize = BondCovLeftSize()
                bondCovLeftSize.bond_code = bond_code
                bondCovLeftSize.date =datetime.strptime(data[0], '%Y-%m-%d').date()
                bondCovLeftSize.left_size = data[1]
                leftSizes.append(bondCovLeftSize)          
            
        return leftSizes
       
    except Exception as e:
        logger.exception(e)
        return []
        
    

