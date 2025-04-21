class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        '''
        1 -3 4 =>> summation = 2 1...6

        length=4

        a b c d

        b-a=1 -> (a,b) 1,2 2,3 3,4 4,5 5,6 b=a+diff
        c-b=-3 -> (b,c) 4,1 5,2 6,3 c=b+diff
        d-c=4 -> (c,d) 1,5 2,6

        3,4,1,5
        4,5,2,6

        s   e   prefix_sum
        3   6   4
            2
        '''
        prefix_sum=0
        s,e=lower, upper
        for diff in differences:
            prefix_sum+=diff
            # if e<s:
            #     return 0
            if prefix_sum+e>upper:
                e=upper-prefix_sum
            elif prefix_sum+s<lower:
                s=lower-prefix_sum

        return e-s+1 if e-s+1>0 else 0

        # for i in range(lower, upper+1):
        #     curr=i
        #     for diff in differences:
        #         curr+=diff
        #         if curr<lower or curr>upper:
        #             break
        #     if lower<=curr<=upper:
        #         cnt+=1

        # return cnt
