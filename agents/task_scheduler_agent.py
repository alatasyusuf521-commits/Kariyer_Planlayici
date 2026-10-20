import datetime
import json


# takvim oluşturucu ajan sınıfı tanımla
class TaskSchedulerAgent:
    def __init__(self, weeks = 4):
        self.weeks = weeks
    
    def create_schedule(self, roadmap):
        today = datetime.date.today()
        
        schedule = {}
        
        for i, step in enumerate(roadmap.get("adımlar", [])):
            
            week = i% self.weeks
            
            
            start_date = today + datetime.timedelta(days = 7*week)
            
            
            if f"Hafta {week+1}" not in schedule:
                schedule[f"Hafta {week+1}"] = []
                
                
                schedule[f"Hafta {week+1}"].append({
                    "gorev":step,
                    "baslangic": str(start_date)
                })
            
        return schedule
    
    
    def save_schedule(self, schedule, filename = "schedule.json"):
        
        with open(filename, "w", encoding = "utf-8") as f:
            
            json.dump(schedule, f, ensure_ascii = False, indent = 2)
            