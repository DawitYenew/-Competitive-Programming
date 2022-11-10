class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        one_counter = 0
        zero_counter = 0
        while right < len(nums):
            if nums[right] == 0:
                zero_counter += 1
            while zero_counter > 1:
                if nums[left] == 0:
                    zero_counter -= 1
                left += 1
            right += 1
            one_counter = max(one_counter, right - left - 1)
        return one_counter
            
