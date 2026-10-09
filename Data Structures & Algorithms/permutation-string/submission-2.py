class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        s1_sorted = sorted(s1) 
        
        for left in range(len(s2) - window_size + 1):
            right = left + window_size
            
            if sorted(s2[left:right]) == s1_sorted:
                return True
        
        return False