class Solution {
public:
    string countAndSay(int n) {
        string s="1";
        int k=1;

        while(k<n){
            char prev=s[0];
            int count=1;
            string ans="";

            for(int i=1;i<s.size();++i){
                if(s[i]==prev){
                    count++;
                }else{
                    ans+=to_string(count) + prev;
                    prev=s[i];
                    count=1;
                }
            }
            ans+=to_string(count)+prev;
            s=ans;
            ++k;
        }

        return s;
    }
};