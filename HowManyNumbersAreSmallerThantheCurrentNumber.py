class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counted = []
        sortedNum = sorted(nums)
        bucket_dic = {}

        for x in range(len(nums)):
            if sortedNum[x] not in bucket_dic:
                bucket_dic[sortedNum[x]]=x
        for i in nums:
            counted.append(bucket_dic[i])
        return counted
