class Solution {
public:
    int trap(vector<int>& height) {
        int left=0, right=height.size()-1;
        int ans=0;
        int max_left=0, max_right=0;
        while(left<right){
            if(height[left]<height[right]){
                height[left]>=max_left ? (max_left=height[left])
                                        : ans+=(max_left-height[left]);
                ++left;
            }else{
                height[right]>=max_right ? (max_right=height[right])
                                        : ans+=(max_right-height[right]);
                --right;
            }
        }
        return ans;
    }
};