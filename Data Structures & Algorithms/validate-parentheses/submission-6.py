class Solution:
    def isValid(self, s: str) -> bool:
        openers = "[{("
        closers = "]})"
        bracket_stack = []
        count_open = 0
        count_close = 0

        if s[0] in closers or s[len(s) - 1] in openers:
            return False

        for i in range(len(s)):
            if s[i] in openers:
                bracket_stack.append(s[i])
                count_open += 1
            if s[i] in closers:
                count_close += 1
                if not bracket_stack or closers.index(s[i]) != openers.index(bracket_stack.pop()):
                    return False
        
        if count_open == count_close:
            return True
        else:
            return False
            
            
            
            