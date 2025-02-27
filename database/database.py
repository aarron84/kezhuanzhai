'''
Author: aarron84 aarron84@qq.com
Date: 2025-02-20 18:25:31
LastEditors: aarron84 aarron84@qq.com
LastEditTime: 2025-02-21 12:44:48
FilePath: /kezhuanzhai/database/database.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from typing import  Type,  TypeVar,  Generic,  List,  Optional
from sqlalchemy import create_engine, insert,  select,  update
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from .config import DatabaseConfig


class BaseModel(DeclarativeBase):
    # __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    pass

class DatabaseSession:
    _engine = create_engine(DatabaseConfig.get_db_uri())
    _session_factory = sessionmaker(bind = _engine)
    
    @classmethod
    def get_session(cls) -> Session:
        return cls._session_factory()
        
    @classmethod
    def init_db(cls) :
        with cls._engine.begin() as conn:                    
            BaseModel.metadata.create_all(conn, checkfirst=True)
            

T = TypeVar("T",  bound=BaseModel)
class Database(Generic[T]):
    def __init__(self, session,  model: Type[T]):         
        self.model = model
        self.session = session
        
    def get(self, **filters):        
        stemt = select(self.model).filter_by(**filters)
        result = self.session.execute(stemt)
        return result.scalar_one_or_none()
        
    def get_all(self, filters)  -> Optional[T]:       
        stemt = select(self.model).filter(filters)
        result = self.session.execute(stemt)
        return result.scalars().all()           


    def add(self, obj):      
        self.session.add(obj)
        self.session.commit()

    def add_all(self, objs): 
        self.session.add_all(objs)
        self.session.commit()
            
    def bulk_add(self, objs):        
        self.session.execute(insert(self.model),  objs)
        self.session.commit()
        
   


        
        
        


