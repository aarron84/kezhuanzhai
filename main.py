# -*- coding: utf-8 -*-
'''
Author: aarron84 aarron84@qq.com
Date: 2025-02-19 13:02:05
LastEditors: aarron84 aarron84@qq.com
LastEditTime: 2025-02-20 17:33:33
FilePath: /kezhuanzhai/main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import akshare as ak
from model.bondCov import BondCov
from database import Database,  DatabaseSession
from service import  BondCovService,  BondCovDailyService
import traceback,  time


DatabaseSession.init_db()
with DatabaseSession.get_session() as session:    
    bondCovService = BondCovService(session)
    bondCovDailyService = BondCovDailyService(session)  
    
    bondCovs = bondCovService.getAll()
    i = 0
    for item in bondCovs:  
        print(f"bond_code = {item.bond_code}")
        bondCovDailyService.getListAndSaveFromOther(item)       
        i+=1
        if i % 3 == 0:
            time.sleep(1)
