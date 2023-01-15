'''
if the given number is divisible by 3 and the quetient is 1 when divided it, then the number is power of 3
else it is not
'''
class Solution:
    def isPowerOfThree(n: int) -> bool:
        if n == 1:
            return True
        if n%3 != 0 or n == 0:
            return False
        return sol.isPowerOfThree(n/3)
    
sol = Solution  
print(sol.isPowerOfThree(9))
print(sol.isPowerOfThree(15))