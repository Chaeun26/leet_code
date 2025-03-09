class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        count=l=0
        n=len(colors)

        for r in range(n+k-1):
            if colors[r%n]==colors[(r-1)%n]:
                l=r
            if r-l+1==k:
                count+=1
                l+=1
            

        return count