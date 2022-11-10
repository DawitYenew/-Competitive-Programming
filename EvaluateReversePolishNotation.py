import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        operators = {'+', '-', '*', '/'}
        if len(tokens) == 1:
            return int(tokens[0])

        for symbol in tokens:
            if symbol not in operators:
                stack.append(int(symbol))
            else:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                result = 0
                if symbol == '+':
                    result = operand_1 + operand_2
                elif symbol == '*':
                    result = operand_1 * operand_2
                elif symbol == '/':
                    result = operand_1 / operand_2
                    result = math.trunc(result)
                elif symbol == '-':
                    result = operand_1 - operand_2
                stack.append(result)
                
        return stack.pop()
