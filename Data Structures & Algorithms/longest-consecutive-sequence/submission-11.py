class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # Remove duplicates first, THEN sort
        nums = sorted(list(set(nums)))
        
        longest_streak = 1
        current_streak = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            else:
                # Update the longest streak and reset the current streak
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
                
        # One final check in case the longest streak was at the very end
        return max(longest_streak, current_streak)