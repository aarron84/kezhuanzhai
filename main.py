# -*- coding: utf-8 -*-
'''
Author: aarron84 aarron84@qq.com
Date: 2025-02-19 13:02:05
LastEditors: aarron84 aarron84@qq.com
LastEditTime: 2025-02-20 17:33:33
FilePath: /kezhuanzhai/main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import logging
try:
    import akshare as ak

    from database import Database,  DatabaseSession
    from service import  BondCovService,  BondCovDailyService, BondCovLeftSizeService
    import   time
    from datetime import datetime
    import jisilu as js
    from model import  BondCov, BondCovDaily

    import sys
    import os
    from sqlalchemy import and_,  or_
    import pandas as pd
    from utils import Logger,  appLogger 
    def test(text,  *msg):
        print(f"text={text} msg={msg is None}")
        

    #
#    bond_zh_cov_df = ak.bond_zh_cov_info_ths()
##    pd.set_option('display.max_columns', None)
##    pd.set_option('display.width', None)
##    pd.set_option('display.max_colwidth', None)
#    print(bond_zh_cov_df[["债券代码", "债券简称", "转股价格"]].to_string())
#    bond_zh_cov_df = ak.bond_zh_cov()
#    print(bond_zh_cov_df[["债券代码", "债券简称", "转股价"]].to_string())

    DatabaseSession.init_db()
        
    try:
        with DatabaseSession.get_session() as session:   
            bondCovService = BondCovService(session)
            bondCovDailyService = BondCovDailyService(session)
            bondCovLeftSizeService = BondCovLeftSizeService(session)
            
            bondCovDailyService.test()
            
#            bondCovService.collectBondCov()
#            bondCovService.updateMaturityDate()
#            bondCovDailyService.collectAllBondCovDaily()
#            bondCovLeftSizeService.collectBondCovLeftSizs()

            
    except Exception as e:
        logging.exception(e)
      
    print("end")
except Exception as e:
    logging.exception(e)
