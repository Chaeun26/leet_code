from collections import deque
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList)==0 or len(secondList)==0:
            return []
        
        firstList=deque(firstList)
        secondList=deque(secondList)
        ans=[]

        first_s,first_e=firstList.popleft()
        second_s,second_e=secondList.popleft()
        
        while True:
            if first_e>=second_s and second_e>=first_s:
                ans.append([max(first_s,second_s),min(first_e,second_e)])


            if firstList and first_e<second_e:
                first_s,first_e=firstList.popleft()
            elif secondList and second_e<first_e:
                second_s,second_e=secondList.popleft()
            elif firstList and secondList:
                first_s,first_e=firstList.popleft()
                second_s,second_e=secondList.popleft()
            else:
                break

                
        return ans

        # ans=[]
        # i=j=0

        # while i<len(firstList) and j<len(secondList):
        #     lo=max(firstList[i][0],secondList[j][0])
        #     hi=min(firstList[i][1],secondList[j][1])
        #     if lo<=hi:
        #         ans.append([lo,hi])

        #     if firstList[i][1]<secondList[j][1]:
        #         i+=1
        #     else:
        #         j+=1
        
        # return ans