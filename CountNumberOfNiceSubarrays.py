class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for num in range(len(nums)):
            if nums[num] % 2 != 0:
                nums[num] = 1
            else:
                nums[num] = 0
        
        my_sum_dic = {0:1}
        counter = 0
        pre_sum = 0

        for number in nums:
            pre_sum += number
            if pre_sum - k in my_sum_dic:
                counter += my_sum_dic[pre_sum - k]
            if pre_sum in my_sum_dic:
                my_sum_dic[pre_sum] += 1
            else:
                my_sum_dic[pre_sum] = 1
        print(counter)
        return counter
