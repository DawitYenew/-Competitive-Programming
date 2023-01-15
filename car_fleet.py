from typing import List
            
class Solution:
    def carFleet(target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        mergedList = list(map(lambda x, y:[x,y], position, speed))
        for x,y in sorted(mergedList)[::-1]:
            stk.append((target - x)/y)
            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()
        print(mergedList)
        return len(stk)
sol = Solution
print(sol.carFleet(100,[0,2,4],[4,2,1]))