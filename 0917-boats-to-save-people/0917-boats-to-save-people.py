class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res=0
        people.sort()
        left,right=0,len(people)-1

        while left<=right:
            if people[left]+people[right] <= limit or left==right:
                left+=1
                right-=1
            else:
                right-=1
            res+=1

        return res