class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prev_s=prev_e=None
        count=0

        for s,e in meetings:
            if prev_e==None:
                prev_s=s
                prev_e=e
                continue
            
            if prev_e < s:
                count+=prev_e-prev_s+1
                prev_s=s
                prev_e=e
            else:
                prev_s=min(prev_s,s)
                prev_e=max(prev_e,e)

        count+=prev_e-prev_s+1
        
        return days-count