class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def repair_aval(time,ranks,cars):
            aval_cars=0
            for r in ranks:
                aval_cars+=int((time//r)**0.5)
            return aval_cars>=cars
        
        left,right=1,min(ranks)*cars*cars
        while left<right:
            mid=(left+right)//2
            if repair_aval(mid,ranks,cars):
                right=mid
            else:
                left=mid+1
        
        return left