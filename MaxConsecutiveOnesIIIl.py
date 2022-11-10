class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0,0
        
        for left in range(len(nums)):
            if nums[left] == 0:
                k -= 1
            if k < 0:
                if nums[right] == 0:
                    k += 1
                right += 1
        return left - right + 1
