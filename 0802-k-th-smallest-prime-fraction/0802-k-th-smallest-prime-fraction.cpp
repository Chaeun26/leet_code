class Solution {
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        int n=arr.size();
        double low = 0.0, high = 1.0;
        int num = 0, den = 1;

        while(high-low > 1e-9){
            double mid = (low+high)/2;
            int count=0;
            num=0, den=1;
            int j = 1;

            for(int i=0; i<n-1; ++i){
                while(j<n && (double)arr[i]/arr[j]>mid){
                    ++j;
                }
                if (j==n) break;
                count+=n-j;
                if(arr[i]*den > arr[j]*num){
                    num=arr[i];
                    den=arr[j];
                }
            }

            if(count<k){
                low=mid;
            }else if(count > k){
                high=mid;
            }else{
                return {num,den};
            }
        }

        return {num,den};

    }
};