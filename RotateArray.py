class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        step = k % len(nums)
        start, end = 0, len(nums)-1
        def reverse(start, end):
            while start < end:
                nums[start], nums[end]  = nums[end], nums[start]
                start += 1
                end -= 1
        nums.reverse()
        reverse(0, step - 1)
        reverse(step, len(nums)-1)
