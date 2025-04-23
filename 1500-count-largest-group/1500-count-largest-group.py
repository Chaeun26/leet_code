class Solution:
    def countLargestGroup(self, n: int) -> int:
        '''
        1 2 3 4 5 6 7 8 9 => size 1 largest
        10 11 12 13 14 15 16 17 18 19 => size 2 largest
           20 21 22 23 24 25 26 27 28 29 => size 3 largest
              30 31 32 33 34 35 36 37 38 39
                 40 41 42 43 44 45 46 47 48 49
                    50 51 52 53 54 55 56 57 58 59
                       60 ...
                                90 91 92 93 94 95 96 97 98 99 => size 10 largest
        100 101 102 103 104 105 106 107 108 109
            110 111 112 ...

        XX..X1 ~ xxx9 -> different group / shift to right group (every 10+)

        each group +9 diff
        
        n=13 size 2, largest so count from 13-10+1
        n=27 size 3, largest, so count from 27-10+1=8
        n=105 size 

        '''
        same_sum=defaultdict(int)
        res=0
        curr_max=0

        for i in range(n+1):
            num=i
            curr_sum=0
            while num>0:
                curr_sum+=(num%10)
                num//=10
            if curr_sum>0:
                same_sum[curr_sum]+=1
                if same_sum[curr_sum]>curr_max:
                    res=1
                    curr_max=same_sum[curr_sum]
                elif same_sum[curr_sum]==curr_max:
                    res+=1
        return res