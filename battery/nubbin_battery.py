from battery.battery import Battery
from battery_period import battery_duration



#Creating Nubbin Battery Class
class NubbinBattery(Battery):
    def __init__(self,current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date



    def needs_service(self):
        
        scheduled_service_date = battery_duration(self.last_service_date, 4)
         #scheduled_service_date is the next service date
        if scheduled_service_date < self.current_date:
            return True
        else:
            return False
