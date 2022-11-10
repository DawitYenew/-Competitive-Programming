class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frqElem=[]
        dic = collections.Counter(nums)
        for val, count in dic.items():
            if len(frqElem)<k:
                heapq.heappush(frqElem,(count,val))
            else:
                heapq.heappush(frqElem,(count,val))
                heapq.heappop(frqElem)
        return [val for count, val in frqElem]
