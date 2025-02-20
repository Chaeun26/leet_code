class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses={k:0 for k in range(numCourses)}
        graph={}
        for course,prereq in prerequisites:
            courses[course]+=1
            if prereq not in graph:
                graph[prereq] = [course]
            else:
                graph[prereq].append(course)
        queue=[k for k, v in courses.items() if v == 0]
        ans=[]
        while queue:
            course=queue.pop(0)
            ans.append(course)
            if course in graph:
                for c in graph[course]:
                    courses[c]-=1
                    if courses[c]==0:
                        queue.append(c)
            
        
        return ans if len(ans)==numCourses else []
