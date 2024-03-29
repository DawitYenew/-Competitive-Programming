class Solution:
    def reverseParentheses(self, s: str) -> str:
        if not s:
            return s
        
        stack = []
        for char in s:
            if char != ")":
                stack.append(char)
            else:
                str_together = ''
                while stack and stack[-1] != '(':
                    ch_from_stk = stack.pop()[::-1]
                    print(ch_from_stk)
                    str_together += ch_from_stk
                stack.pop()
                stack.append(str_together)
        return "".join(stack)
                

       
               

