class TimeMap:

    def __init__(self):
        self.time_based_structure=defaultdict(lambda: ([],[]))

    def set(self, key: str, value: str, timestamp: int) -> None:
        timestamps,values=self.time_based_structure[key]
        timestamps.append(timestamp)
        values.append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_based_structure:
            return ""
        timestamps,values=self.time_based_structure[key]
        idx = bisect.bisect_right(timestamps,timestamp)

        return values[idx-1] if idx>0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)