class Solution():
    def PredictTheWinner(self, nums):
        dp = {}
        def find(i, j):
            print(i,j)
            print(dp)
            if (i, j) not in dp:
                if i == j:
                    print(nums[i])
                    return nums[i]
                dp[i,j] = max(nums[i]-find(i+1, j), nums[j]-find(i, j-1))
            return dp[i,j]

        return find(0, len(nums)-1) >= 0
print(Solution().PredictTheWinner([1,5,2]))