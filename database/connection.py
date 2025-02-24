'''
Author: aarron84 aarron84@qq.com
Date: 2025-02-20 13:44:25
LastEditors: aarron84 aarron84@qq.com
LastEditTime: 2025-02-20 13:47:15
FilePath: /kezhuanzhai/sql/connection.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'mysql+pymysql://username:password@localhost/dbname'

# Create an engine
engine = create_engine(DATABASE_URI)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

# Example usage
# result = session.execute("SELECT * FROM some_table")
# for row in result:
#     print(row)

# Don't forget to close the session when done
# session.close()