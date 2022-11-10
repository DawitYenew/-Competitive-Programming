class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        max_heap = [-count for count in task_count.values()]
        print(max_heap)
        heapq.heapify(max_heap)
        print(max_heap)

        time = 0
        que = deque()
        while max_heap or que:
            time += 1
            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    que.append([count, time + n])
            if que and que[0][1] == time:
                heapq.heappush(max_heap, que.popleft()[0])
        return time
