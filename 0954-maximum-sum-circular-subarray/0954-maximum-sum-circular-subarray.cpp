class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int cmax = 0;
        int cmin = 0;
        int maxSum = nums[0];
        int minSum = nums[0];
        int totalSum = 0;

        for(int num:nums){
            cmax=max(cmax,0) + num;
            maxSum=max(maxSum,cmax);
            
            cmin=min(cmin,0) + num;
            minSum=min(minSum,cmin);

            totalSum+=num;
        }

        if(totalSum==minSum){
            return maxSum;
        }

        return max(maxSum, totalSum-minSum);
    }
};