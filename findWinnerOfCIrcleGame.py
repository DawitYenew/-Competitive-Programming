class Solution:
    def findTheWinner(self, n: int, k: int):
        lists = [x for x in range(1, n+1)]
        del_pos = -1 
        if k == 1:
            lists.pop(0)
            return lists
        while n > 1:
            del_pos = (del_pos+k)%n
            lists.pop(del_pos)
            del_pos -= 1
            n -= 1
        return lists[0]



#this one is a solutio using queue
# class Solution:
#     def findTheWinner(self, n: int, k: int):
#         queue = circularQueue(n)
#         # print(queue)
        
#         while queue._len() != 1:
#              self.removePerson(queue,k)
#         return queue.top()
    
#     def removePerson(self, friends, k):
#         if k == 1:
#             friends.pop()
#             print(friends)
#             return friends
#         friends.next()
#         self.removePerson(friends,k-1)
        

# #circualr queue class to access circualr queue
# class circularQueue:
#     def __init__(self,size) -> None:
#         self.c_queue = list()
#         for i in range(1,size+1):
#             self.c_queue.append(i)
#         self._top = 0
#     def _len(self):
#         return len(self.c_queue)
#     def next(self):
#         self._top += 1
#         if self._top >= len(self.c_queue):
#             self._top = 0
        
#     def pop(self):
#         if self.c_queue:
#             self.c_queue.pop(self._top)
#             if self._top >= len(self.c_queue):
#                 self._top = 0
#     def top(self):
#         if self.c_queue:
#             return self.c_queue[self._top]
            
        
sol = Solution()
print(sol.findTheWinner(5,1))