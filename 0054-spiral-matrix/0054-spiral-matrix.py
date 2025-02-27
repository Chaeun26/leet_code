class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        if m==1 and n==1:
            return [matrix[0][0]]
        
        startRow,startCol=0,0
        endRow,endCol=m-1,n-1
        r=c=0
        ans=[]
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        dir_idx=0

        for i in range(m*n):
            ans.append(matrix[r][c])

            tmp_r = r+direction[dir_idx][0]
            tmp_c = c+direction[dir_idx][1]

            if tmp_r<startRow or tmp_r>endRow or tmp_c<startCol or tmp_c>endCol:
                dir_idx=(dir_idx+1)%4
                tmp_r = r+direction[dir_idx][0]
                tmp_c = c+direction[dir_idx][1]
                
                startRow+=1 if dir_idx==1 else 0
                endCol-=1 if dir_idx==2 else 0
                endRow-=1 if dir_idx==3 else 0
                startCol+=1 if dir_idx==0 else 0
                
            r=tmp_r
            c=tmp_c
        
        return ans