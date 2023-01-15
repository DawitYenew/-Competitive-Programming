from typing import List

class Solution:
    def dailyTemperatures(temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stk = []
        for ind, tem in enumerate(temperatures):
            while stk and tem > stk[-1][0]:
                tempVal, tempIndex= stk.pop()
                print(tempIndex)
                ans = ind - tempIndex
                output[tempIndex] = ans    
                print(output)
            stk.append([tem, ind])
        return output

temperature = [89,62,70,58,47,47,46,76,100,70]
sol = Solution
print(sol.dailyTemperatures(temperature))
                
           