# -*- coding: utf-8 -*-
# utils/stockExchange.py

class StockExchange:
    
    exchange = {
        "11":"sh", 
        "12": "sz"
    }
    
 
    
    '''
    通过可转债代码获取可转债所在交易所编号
    '''
    @classmethod
    def get_StockExchange_by_bondCovCode(cls, code: str):
      
        pre = code[0:2]
        return cls.exchange[pre] if pre in cls.exchange else None

        
    '''
    获取交易所编码＋可传债代码
    '''
    @classmethod
    def get_bondCodeWithStockExchange(cls, code: str):
        exchange = cls.get_StockExchange_by_bondCovCode(code)
        if(exchange):
            return exchange + code
        else:
            return code
        
