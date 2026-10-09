class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        # Keep s1 as a sorted list (e.g., ['a', 'b'])
        s1_sorted = sorted(s1) 
        
        # We can simplify the loop bounds using a for-loop
        for left in range(len(s2) - window_size + 1):
            right = left + window_size
            
            # sorted() returns a list, matching s1_sorted
            if sorted(s2[left:right]) == s1_sorted:
                return True
        
        return False