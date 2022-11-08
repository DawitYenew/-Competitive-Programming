class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l, r=0, len(nums)-1

        result = []
        nums.sort()
        while len(result) != len(nums):
            result.append(nums[l])
            l += 1

            if l <= r:
                result.append(nums[r])
                r -= 1
        return result
