class Solution {
    public boolean containsDuplicate(int[] nums) {
        /**SORTING**
        time: O(nlgn) 
        space:O(1)
        
        **MAP**
        time:O(n)
        space:O(n)
        */
        Arrays.sort(nums);
        for(int i=0;i<nums.length-1;i++){
            if(nums[i]==nums[i+1]){
                return true;
            }
        }
        return false;
    }
}
