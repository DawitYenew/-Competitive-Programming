class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        high = len(nums)-1
        r = 0
        while r <= high:
            if nums[r] == 0:
                nums[r], nums[low] = nums[low], nums[r]
                r +=1 
                low +=1
            elif nums[r] == 1:
                r += 1

            elif nums[r] == 2:
                nums[r], nums[high] = nums[high], nums[r]
                high -= 1
        

        
