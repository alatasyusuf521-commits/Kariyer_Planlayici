import json
import os


class UserMemory:
    
    
    def __init__(self, filepath = "memory.json"):
        self.filepath = filepath
        self.memory = self.load_memory()
    
    
    def load_memory(self):
        if os.path.exists(self.filepath):
            
            with open(self.filepath, "r", encoding = "utf-8") as f:
                return json.load(f)
        
        else:
            return { }
        
    
    def save_memory(self):
        with open(self.filepath, "w", encoding = "utf-8") as f:
            json.dump(self.memory, f, ensure_ascii = "False", indent=2)
    
    
    def update_goal(self, goal):
        self.memory["goal"] = goal
        self.save_memory()
    
    
    
    def update_progress(self, week, progress):
        if "progress" not in self.memory:
            self.memory["progress"] = {}
        self.memory["progress"]["week"] = progress
        self.save_memory()
    
    
    def get_momory(self):
        return self.memory