class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m,n=len(mat),len(mat[0])
        
        heights=[[0]*n for _ in range(m)]
        
        for c in range(n):
            for r in range(m):
                if mat[r][c]==1:
                    heights[r][c]=heights[r-1][c]+1
        
        def counting(heights):
            stack=[]
            count=0
            sum_counts=[0]*len(heights)
            
            for i,h in enumerate(heights):
                while stack and stack[-1][0]>=h:
                    stack.pop()
                
                if stack:
                    prev=stack[-1][1]
                    sum_counts[i]=sum_counts[prev] + h*(i-prev)
                else:
                    sum_counts[i]=h*(i+1)
                
                stack.append((h,i))
                count+=sum_counts[i]
                print(i,h,sum_counts[i])
            return count
        
        total=0
        for r in range(m):
            total+=counting(heights[r])
            
        return total