from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites)==0:
            return True
        
        num_of_pre = {i:0 for i in range(numCourses)}
        connections={}

        for i in range(len(prerequisites)):
            if prerequisites[i][0]==prerequisites[i][1]:
                return False
            num_of_pre[prerequisites[i][0]]+=1
            if prerequisites[i][1] in connections:
                connections[prerequisites[i][1]].append(prerequisites[i][0])
            else:
                connections[prerequisites[i][1]]=[prerequisites[i][0]]

        q=deque([k for k,v in num_of_pre.items() if v==0])
        if len(q)==0:
            return False
        count=len(q)
        while q:
            node=q.popleft()
            
            if node in connections:
                for n in connections[node]:
                    num_of_pre[n]-=1
                    if num_of_pre[n]==0:
                        count+=1
                        if count==numCourses:
                            return True
                        q.append(n)
        return False
        
