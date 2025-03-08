class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count=0

        for i in range(k):
            if blocks[i]=='W':
                count+=1
        
        min_count=count
        
        for i in range(1,len(blocks)-k+1):
            if blocks[i-1]=='W':
                count-=1
            if blocks[i+k-1]=='W':
                count+=1
            min_count=min(min_count, count)
        
        return min_count