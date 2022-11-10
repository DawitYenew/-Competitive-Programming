class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        sum_ = 0
        for i in range(len(arr)):
            if i < k - 1:
                sum_ += arr[i]
            elif i == k - 1:
                sum_ += arr[i]
                if sum_/k >= threshold:
                    count += 1
            else:
                sum_ += arr[i]
                sum_ -= arr[i-k] 
                if sum_/k >= threshold:
                    count += 1
        return count



