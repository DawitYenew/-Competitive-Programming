class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_most_sum = 0
        total_sum = sum(nums)
        for i in range(len(nums)):
            right_most_sum = total_sum - nums[i] - left_most_sum
            if right_most_sum == left_most_sum:
                return i
            left_most_sum += nums[i]
        return -1
