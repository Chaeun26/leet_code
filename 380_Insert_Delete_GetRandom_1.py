class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.arr.append(val)
        self.dict[val]=len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            idx=self.dict[val]
            end_val=self.arr[-1]
            self.dict[end_val]=idx
            self.arr[idx]=end_val
            self.arr.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
