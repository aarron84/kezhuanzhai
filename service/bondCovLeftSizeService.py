
from model import BondCovLeftSize,  BondCov
from database import Database
import jisilu as js
from utils import exception_handle
import time

class BondCovLeftSizeService:
    
    def __init__(self,  session):  
        self.session = session
        self.bondCovLeftSize_dal = Database(session, BondCovLeftSize)
        self.bondCov_dal =Database(session,  BondCov)
    
    @exception_handle
    def  collectBondCovLeftSizs(self):
        bonds = self.bondCov_dal.get_all()      
        for bond in bonds:            
            leftsizes = js.bond_left_size(bond.bond_code)           
            size = bond.left_size
            lastDate = self.getMaxDate(bond.bond_code)
            noExistLeftSizes = []
            for item in leftsizes:              
                #已添加过剩余规模
                if lastDate != None and item.date <= lastDate:   
                    continue
                noExistLeftSizes.append(item)
                item.bond_id = bond.id
                if bond.left_size > item.left_size:
                    bond.left_size = item.left_size
            if noExistLeftSizes:
                self.bondCovLeftSize_dal.bulk_add(noExistLeftSizes)
            time.sleep(1)
    
    def getMaxDate(self, bond_code):
            return self.bondCovLeftSize_dal.getMax(BondCovLeftSize.date,  BondCovLeftSize.bond_code == bond_code)
            
        
