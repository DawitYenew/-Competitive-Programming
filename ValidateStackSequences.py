class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pushed_st, end=0, len(pushed)-1
        popped_st =0
        
        for i in range(len(pushed)):
            pushed_st = i
            stack.append(pushed[pushed_st])
        
            while stack[-1] == popped[popped_st]:
                stack.pop(-1)
                popped_st += 1
                if not stack:
                    break
            if pushed_st == end and not stack:
                return True
        return False

