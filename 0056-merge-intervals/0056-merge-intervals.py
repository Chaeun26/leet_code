class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals

        intervals.sort()
        s,e = intervals[0]
        ans=[]

        for i in range(1,len(intervals)):
            curr_s,curr_e = intervals[i]

            if e < curr_s:
                ans.append([s,e])
                s=curr_s
                e=curr_e
            else:
                s=min(s, curr_s)
                e=max(e,curr_e)
        ans.append([s,e])
        return ans