class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec=[]

        for v in vec:
            for mem in v:
                self.vec.append(mem)
        self.idx=0
        self.n=len(self.vec)

    def next(self) -> int:
        res = self.vec[self.idx]
        self.idx+=1
        return res
    def hasNext(self) -> bool:
        return self.idx < self.n

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()