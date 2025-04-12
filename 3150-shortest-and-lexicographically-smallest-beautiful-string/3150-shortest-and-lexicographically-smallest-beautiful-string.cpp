#include <iostream>
#include <string>

class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        int start=0;
        int shortest=1e9;
        int curr_count=0;
        string res="";

        for(int i=0; i < s.length(); ++i){
            if(s[i]=='1'){
                curr_count+=1;
            }
            while(curr_count==k){
                string candi=s.substr(start,i-start+1);
                if(i-start+1<shortest || (i-start+1==shortest && candi < res)){
                    res=candi;
                    shortest=i-start+1;
                }
                if(s[start]=='1'){
                    curr_count-=1;
                }
                start+=1;
            }
        }

        return res;
    }
};