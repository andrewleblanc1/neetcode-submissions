class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.timeMap.get(timestamp) is None:
            self.timeMap.update({timestamp:{}})
        self.timeMap.get(timestamp).update({key:value})
        

    def get(self, key: str, timestamp: int) -> str:
        while timestamp >= 0:
            time = self.timeMap.get(timestamp)
            if time is not None and time.get(key) is not None:
                return time.get(key)
            timestamp -= 1
        return ""
        
