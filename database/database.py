'''
Author: aarron84 aarron84@qq.com
Date: 2025-02-20 18:25:31
LastEditors: aarron84 aarron84@qq.com
LastEditTime: 2025-02-21 12:44:48
FilePath: /kezhuanzhai/database/database.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from .config import DatabaseConfig


class Base(DeclarativeBase):
    # __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'}
    pass

class Database:
    def __init__(self):    
        self.engine = create_engine(DatabaseConfig.get_db_uri())
        self.session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.session()

    def init_db(self):
        Base.metadata.create_all(self.engine, checkfirst=True)

    def drop_db(self):
        Base.metadata.drop_all(self.engine)

    def add(self, obj):
        with self.get_session() as session:
            session.add(obj)
            session.commit()

    def add_all(self, objs):
        with self.get_session() as session:
            session.add_all(objs)
            session.commit()
    def bulk_add(self, model, objs):
        with self.get_session() as session:
            session.execute(insert(model),  objs)
            session.commit()

    def query(self, model, **kwargs):
        with self.get_session() as session:
            return session.query(model).filter_by(**kwargs).all()

        
        
        


