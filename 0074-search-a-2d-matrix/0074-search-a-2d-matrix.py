class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        if m==1 and n==1:
            return True if matrix[0][0]==target else False
        i=0
        j=m*n-1

        while i<=j:
            mid=(i+j)//2

            midr=mid//n
            midc=mid%n

            print(i,j,midr,midc)

            if matrix[midr][midc] < target:
                i=mid+1
            elif matrix[midr][midc] > target:
                j=mid-1
            else:
                return True
        
        return False