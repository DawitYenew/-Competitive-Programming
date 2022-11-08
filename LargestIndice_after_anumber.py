class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(nums)
        target_index = []
        for i in range(len(sortedNums)):
            if sortedNums[i] == target:
                target_index.append(i)
        return target_index
