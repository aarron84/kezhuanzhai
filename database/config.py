'''
Author: aarron84 aarron84@qq.com
Date: 2025-02-20 17:45:55
LastEditors: aarron84 aarron84@qq.com
LastEditTime: 2025-02-20 18:37:56
FilePath: /kezhuanzhai/database/config.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
'''
Author: aarron84 aarron84@qq.com
Date: 2025-02-20 17:45:55
LastEditors: aarron84 aarron84@qq.com
LastEditTime: 2025-02-20 17:50:56
FilePath: /kezhuanzhai/database/config.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class DatabaseConfig:
    DB_NAME = 'Kezhuanzhai'
    DB_USER = 'root'
    DB_PASSWORD = 'aarron84'
    DB_HOST = 'localhost'
    DB_PORT = '3306'

    @classmethod
    def get_db_uri(cls):
        return f'mysql+pymysql://{cls.DB_USER}:{cls.DB_PASSWORD}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}'
   
