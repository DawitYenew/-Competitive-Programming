class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        print(intervals)
        result = [intervals[0]]

        for st, end in intervals[1:]:
            if st <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([st,end])
        return result
        
