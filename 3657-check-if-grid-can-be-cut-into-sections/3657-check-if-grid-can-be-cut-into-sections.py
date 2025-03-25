class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x_ranges=[]
        y_ranges=[]

        for sx,sy,ex,ey in rectangles:
            x_ranges.append((sx,ex))
            y_ranges.append((sy,ey))

        x_ranges.sort()
        y_ranges.sort()

        def cut_possibility(ranges):
            latest_end=count=0
            for s,e in ranges:
                if 0 < latest_end <= s:
                    count+=1
                latest_end=max(latest_end,e)

            return count
        
        return cut_possibility(x_ranges)>=2 or cut_possibility(y_ranges)>=2