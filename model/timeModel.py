# -*- coding: utf-8 -*-
# model/timeModel.py
import datetime
from sqlalchemy import DateTime, Integer,  func
from sqlalchemy.orm import Mapped,  mapped_column 
from database import  BaseModel

class TimeModel(BaseModel):
    __abstract__ = True
#      id =  Column(Integer, primary_key=True, autoincrement=True)
    id:Mapped[int] = mapped_column(Integer,  primary_key=True,  autoincrement=True)
    create_at: Mapped[datetime] = mapped_column(DateTime,  default = func.now(),   nullable = False)
    update_at: Mapped[datetime] = mapped_column(DateTime, default = func.now(),  onupdate = func.now() , nullable = False)
