class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        '''

        10 50 55 120 140 210
              i
        0 15 60 70
             j   

        start1 > end2 e.g., 30 10
        start2 > end1 e.g., 50 15

        if interset -> check earlist start time ... 60 (max of start) check start+duration <= min finish
        duration=12

        10 50 60 120 140 210
              i
        0 5 20 30 50 70
                  j

        start_time  fin_time
        20+12 >         30
        60              70

        [[216,397,070 ,363,167,701],[98,730,764,158208909],[441003187,466254040],[558239978,678368334],[683942980,717766451]]

        [[50,490,609 ,222,653,186],[512711631,670791418],[730229023,802410205],[812553104,891266775],[230032010,399152578]]
        '''

        slots1.sort()
        slots2.sort()

        n1,n2=len(slots1),len(slots2)
        i=j=0

        while i<n1 and j<n2:
            if slots1[i][0] > slots2[j][1] or slots2[j][0] > slots1[i][1]:
                if slots1[i][1]<slots2[j][1]:
                    i+=1
                else:
                    j+=1

            else:
                start_time=max(slots1[i][0],slots2[j][0])
                fin_time=min(slots1[i][1],slots2[j][1])
                if start_time+duration <= fin_time:
                    return [start_time,start_time+duration]
                else:
                    if slots1[i][1]<slots2[j][1]:
                        i+=1
                    else:
                        j+=1


        return []