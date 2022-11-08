class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        p_heap = []
        for x,y in points:
            distance = (x ** 2) +(y ** 2)
            p_heap.append([distance, x, y])
        
        heapq.heapify(p_heap)
        kClosest = []
        while k > 0:
            distance,x ,y = heapq.heappop(p_heap)
            kClosest.append([x,y])
            k -= 1
        return kClosest

