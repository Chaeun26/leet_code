class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''

        n objects, color: red, while, blue
        same color-> adjacent

        red-white-blue
        0-1-2

        similar to tower of hanoi?

        2 0 2 1 1 0



        0 0 1 1 2 2
        '''

        nums.sort()