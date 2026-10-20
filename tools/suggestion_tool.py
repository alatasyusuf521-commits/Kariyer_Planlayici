from ddgs import DDGS

class SuggestionTool:
    def __init__(self):
        self.ddgs = DDGS()
    
    
    def search_resources(self, query, max_results = 5):
        
        results = self.ddgs.text(query, max_results = max_results)
        
        
        suggestion = []
        
        
        for item in results:
            
            suggestion.append({
                "title": item.get("title"),
                "link": item.get("href"),
                "snipped": item.get("body")
            })
        
        return suggestion

# a = SuggestionTool()