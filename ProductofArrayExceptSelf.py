class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_list = [0]*len(nums)
        prefix = 1
        postfix=1 
        for i in range(len(nums)):
            prod_list[i] = prefix
            prefix *= nums[i]
        for i in reversed(range(len(nums))):
            prod_list[i] *= postfix
            postfix *= nums[i]
        
        return prod_list
