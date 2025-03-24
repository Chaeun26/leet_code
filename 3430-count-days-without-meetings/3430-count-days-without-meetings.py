class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prev_s,prev_e=meetings[0]
        count=0

        for i in range(1,len(meetings)):
            if prev_e < meetings[i][0]:
                count+=prev_e-meetings[i][0]+1
                prev_e=meetings[i][1]
            else:
                prev_e=max(prev_e,meetings[i][1])

        count+=prev_e-prev_s+1

        return days-count