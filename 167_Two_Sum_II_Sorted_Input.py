class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        maps={}
        for i in range(len(numbers)):
            if target - numbers[i] in maps:
                return [maps[target-numbers[i]],i+1]
            maps[numbers[i]]=i+1
