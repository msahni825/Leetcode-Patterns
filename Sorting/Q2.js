/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    // nums.sort()
    let ans=0
    for(let i=0;i<nums.length;i++){
        ans+=nums[i]-i
    }
    return nums.length-ans;
};
