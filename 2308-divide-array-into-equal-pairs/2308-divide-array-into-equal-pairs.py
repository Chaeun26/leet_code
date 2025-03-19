class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mem=set()

        for num in nums:
            if num in mem:
                mem.remove(num)
            else:
                mem.add(num)
        
        return True if len(mem)==0 else False