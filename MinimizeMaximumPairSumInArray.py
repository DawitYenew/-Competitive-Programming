class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        nums.sort()
        sums = 0
        while l < r:
            sums = max(nums[l] + nums[r], sums)
            l += 1
            r -= 1
        return sums

