# -*- coding: utf-8 -*-
# database/BaseModel.py
from sqlalchemy.orm import DeclarativeBase, class_mapper
DeclarativeBase
class BaseModel(DeclarativeBase):
    # __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    def __getitem__(self, item):        
        return getattr(self, item)
    
    def keys(self):
        mapper = class_mapper(type(self))        
        return {prop.key: None for prop in mapper.iterate_properties}.keys()
            
