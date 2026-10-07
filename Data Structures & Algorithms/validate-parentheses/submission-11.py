class Solution:
    def isValid(self, s: str) -> bool:
        openers = "{[("
        closers = "}])"
        bracket_stack = []
        o_count = 0
        c_count = 0

        for i in range(len(s)):
            if s[i] in openers:
                bracket_stack.append(s[i])
                o_count += 1
            if s[i] in closers:
                c_count += 1
                if not bracket_stack or closers.index(s[i]) != openers.index(bracket_stack.pop()):
                    return False
        
        return o_count == c_count