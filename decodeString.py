class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
       
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
                print(stack)
            else:
                string = ""
                while stack[-1] != "[":
                    string = stack.pop() + string
                    print(string)
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                    print(k)
                stack.append(int(k) * string)
                print(stack)
        return "".join(stack)
s = "3[a]2[bc]"
print(Solution().decodeString(s))