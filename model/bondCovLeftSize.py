from sqlalchemy import Column, Integer,  Float, String,  Date,  ForeignKey
from .timeModel import  TimeModel

class BondCovLeftSize(TimeModel):
    __tablename__ = 'bond_cov_left_size'
    id =  Column(Integer, primary_key=True, autoincrement=True)
    bond_code =  Column(String(10), index=True)
    bond_id = Column(Integer, ForeignKey('bond_cov.id'), index=True)
    date =  Column(Date)
    left_size = Column(Float)
