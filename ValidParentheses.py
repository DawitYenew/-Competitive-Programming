class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dic = {'(':')', '[':']', '{':'}'}
        for ch in s:
            if ch in bracket_dic.keys():
                stack.append(ch)
            else:
                if stack ==  []:
                    return False
                is_open = stack.pop()
                if ch != bracket_dic[is_open]:
                    return False
        return stack == []
