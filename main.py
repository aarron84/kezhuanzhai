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
from database import Database
import math
database = Database()
database.init_db()
bond_zh_cov_df = ak.bond_zh_cov()
bonds = [];
for index , row in bond_zh_cov_df.iterrows():
    bond = BondCov(bond_code = row['债券代码'], name=row['债券简称'])
    bond.stock_code = row['正股代码']
    bond.stock_name = row['正股简称']
    bond.issue_size = row['发行规模']
#   if math.isnan(row['转股价']):
#        bond.conversion_price  = None
#    else:
#        bond.conversion_price = row['转股价'] 
        
    bond.conversion_price = row['转股价']
    bond.conversion_price = None if math.isnan(bond.conversion_price) else bond.conversion_price
    if math.isnan(row['转股价']):
        print(f'转股价={ bond.conversion_price }')
    bond.list_date = row['上市时间']
    bond.credit_rating = row['信用评级']
    bonds.append(bond)
    database.add(bond)

#database.add_all(bonds)
print('end')
#print(bond_zh_cov_df)
#comparison = ak.bond_zh_cov_info_ths()
#print(comparison)
