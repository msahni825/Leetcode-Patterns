class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int ans=-1;
        int i=0;
        int n=nums.size();
        sort(nums.begin(),nums.end());//O(nlgn)
        if(i==0 && nums[i]!=0){
            ans=0;
            return ans;
        }
        for(i=0;i<n;i++){//0,1,3
            if(i!=n && nums[i]!=i){
                ans=i;
                return ans;
            }
        }
        if(i==n && ans==-1){
            ans=n;
        }
        return ans;
    }
};
