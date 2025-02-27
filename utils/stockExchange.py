# -*- coding: utf-8 -*-
# utils/stockExchange.py

class StockExchange:
    
    shang_hai ='sh'
    shenzhen = 'sz'
    @classmethod
    def get_StockExchange_by_bondCovCode(cls, code: str):
        if code.startswith("11"):
            return cls.shang_hai
        elif code.startswith("12"):
            return cls.shenzhen
        
        return None
    @classmethod
    def get_bondCodeWithStockExchange(cls, code: str):
        exchange = cls.get_StockExchange_by_bondCovCode(code)
        if(exchange):
            return exchange + code
        else:
            return code
        
