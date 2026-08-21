class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        temp = self.data.get(key)
        if not temp:
            return ""
        
        low = 0
        high = len(temp) - 1
        result = -1
        while low <= high:
            mid = low + (high - low)//2

            if temp[mid][1] <= timestamp:
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        if result == -1: return ""
        else:
            return temp[result][0] 