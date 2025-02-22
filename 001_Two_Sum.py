class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps={}
        
        for i,n in enumerate(nums):
            if n in maps:
                return [maps[n],i]
            else:
                maps[target-n]=i
        
        return []
