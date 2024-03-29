class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = []
        min_sum = len(nums) + 1
        pre_sum = [0 for i in range(len(nums)+1)]
        for i in range(len(nums)):
            pre_sum[i + 1] = pre_sum[i] + nums[i]
           
        for j in range(len(pre_sum)):
            while len(queue) > 0 and pre_sum[j] <= pre_sum[queue[-1]]:
                queue.pop()
            while len(queue) > 0 and pre_sum[j] >= pre_sum[queue[0]] + k:
                min_sum = min(min_sum, j - queue.pop(0))
            queue.append(j)
        return min_sum if min_sum < len(nums)+1 else -1
        
