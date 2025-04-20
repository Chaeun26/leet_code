class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        seen=defaultdict(int)
        res=0

        for ans in answers:
            if ans not in seen:
                res+=ans+1
            else:
                if seen[ans]>=ans+1:
                    seen[ans]=0
                    res+=ans+1
            seen[ans]+=1
        return res

        '''
        1 0 1 0 0 

        res=3
        seen: 1:2 0:1
        '''