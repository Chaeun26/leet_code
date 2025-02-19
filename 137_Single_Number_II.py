class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        maps={}

        for n in nums:
            if n not in maps:
                maps[n]=1
            else:
                maps[n]+=1

        for key in maps:
            if maps[key]==1:
                return key

# Bit Manipulation ver.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        first=second=0

        for n in nums:
            first = (first ^ n) & (~second)
            second = (second ^ n) & (~first)
        
        return first
