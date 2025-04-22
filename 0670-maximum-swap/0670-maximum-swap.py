class Solution:
    def maximumSwap(self, num: int) -> int:
        '''

        2 7 3 6

        2 -> 7: 2<7 ... 72 36

        7 2 3 6

        7 2 6 6
        7662 / 7626

        num = 7 2 3 6

        check whether maximum number is in the first -> check 2nd largest one is in 2nd -> check 3rd is in 3rd ....

        [7,2,3,6] -> sort in reverse [7 6 3 2]
        compare one by one from the first =>> 7 : 7 -> 2 : 6 Different => 7 6 3 2
        '''
        if num<=10:
            return num

        num_list=[c for c in str(num)]


        for i in range(len(num_list)-1):
            max_num=max(num_list[i+1:])
            if num_list[i] < max_num:
                for j in range(len(num_list)-1,i,-1):
                    if num_list[j]==max_num:
                        tmp=num_list[i]
                        num_list[i]=num_list[j]
                        num_list[j]=tmp
                        return int(''.join(num_list))

        return int(''.join(num_list))


