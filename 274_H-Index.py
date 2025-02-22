class Solution:
    def hIndex(self, citations: List[int]) -> int:
        maps={k:0 for k in range(len(citations)+1)}

        for paper in citations:
            for p in range(paper,-1,-1):
                if p in maps:
                    maps[p]+=1
        ans=0
        for key,value in maps.items():
            if value>=key:
                ans=max(ans,key)

        return ans

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans=0
        for i,c in enumerate(citations):
            if c>=i+1:
                ans+=1
            else:
                break
        return ans
