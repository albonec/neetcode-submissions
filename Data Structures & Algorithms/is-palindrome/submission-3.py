class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join([c for c in s.lower() if c.isalnum()])
        low = 0
        high = len(clean) - 1

        while low < high:
            if clean[low] == clean[high]:
                low += 1
                high -= 1
            else:
                return False
        return True
            