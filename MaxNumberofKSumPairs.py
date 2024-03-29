class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r=0, len(nums)-1
        num_op = 0
        while l < r:
            sums = nums[l] + nums[r]
            if sums == k:
                num_op += 1
                l += 1
                r -= 1
            elif sums < k:
                l += 1
            else:
                r -= 1
        return num_op
