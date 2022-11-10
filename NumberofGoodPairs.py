class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        visited = {}
        count = 0
        for num in nums:
            if num in visited:
               count += visited[num]
               visited[num] += 1
            else:
                visited[num] = 1
        return count

                
           
