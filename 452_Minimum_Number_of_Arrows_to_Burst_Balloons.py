class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        sorted_points = sorted(points, key=lambda point:point[1])

        arrow=sorted_points[0][1]
        count=1
        for i in range(1, len(points)):
            if sorted_points[i][0] > arrow or arrow > sorted_points[i][1]:
                arrow = sorted_points[i][1]
                count+=1
        
        return count
