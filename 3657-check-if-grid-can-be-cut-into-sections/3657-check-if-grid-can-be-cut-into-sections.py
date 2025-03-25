class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        def cut_possibility(rect,dim):
            count=0
            rect.sort(key=lambda rect:rect[dim])
            latest_end=rect[0][dim+2]
            for i in range(1,len(rect)):
                if latest_end <= rect[i][dim]:
                    count+=1
                latest_end=max(latest_end,rect[i][dim+2])

            return count>=2
        
        return cut_possibility(rectangles,0) or cut_possibility(rectangles,1)