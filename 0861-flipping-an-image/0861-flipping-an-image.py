class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n=len(image)
        
        for r in range(n):
            for c in range((n+1)//2):
                tmp=image[r][c]^1
                image[r][c]=image[r][~c]^1
                image[r][~c]=tmp
        
        return image