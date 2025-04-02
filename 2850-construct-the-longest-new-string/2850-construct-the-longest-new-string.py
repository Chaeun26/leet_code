class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        As = min(x,y+1)
        Bs = min(x+1,y)

        ABs = z

        return (As + Bs + ABs)*2