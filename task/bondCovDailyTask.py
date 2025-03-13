from service import  BondCovService, BondCovDailyService
from database import  DatabaseSession
import time
class BondCovDailyTask:
    def run(self):       
        
        with DatabaseSession.get_session() as session:               
            bondCovService = BondCovService(session)
            bondCovDailyService = BondCovDailyService(session)              
            bondCovs = bondCovService.getAll()
            i = 0
            for item in bondCovs:              
                bondCovDailyService.getListAndSaveFromOther(item)       
                i+=1
                if i % 3 == 0:
                    time.sleep(1)
