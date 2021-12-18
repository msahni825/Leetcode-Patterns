class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in range(len(nums)):
            # print(xor)
            xor ^= (i+1)^nums[i]
            print(xor)
        return xor
    
#     [3,0,1]
#     xor=0
#     i=0 to 3
    
#     i=0
#     xor^=(1)^nums[0]    
#     xor^=1(1^3)
    
#     i=1
#     xor^=(2)^nums[1] 
#     xor^=1(2^0)
    
#     i=2
#     xor^=(3)^nums[2] 
#     xor^=3(3^1)
