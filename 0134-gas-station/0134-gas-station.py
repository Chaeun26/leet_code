class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        total=ans=0
        minimum = float('inf')
        for i in range(n):
            total += gas[i]-cost[i]
            if total < minimum:
                minimum=total
                ans=(i+1)%n
        return -1 if total < 0 else ans
