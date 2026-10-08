class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for tok in tokens:
            if tok == "+":
                right = stack.pop()
                left = stack.pop()
                stack.append(left + right)
            elif tok == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)
            elif tok == "*":
                right = stack.pop()
                left = stack.pop()
                stack.append(left * right)
            elif tok == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left / right)) 
            else:
                stack.append(int(tok))
                
        return stack[0]