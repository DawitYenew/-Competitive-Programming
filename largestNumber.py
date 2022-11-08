class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        def comp(a,b):
            if a + b > b + a:
                return -1
            else:
                return 1
        nums = sorted(nums, key=cmp_to_key(comp))
        return str(int("".join(nums)))

         
