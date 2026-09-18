class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 1. Manually count frequencies 
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
                
        # 2. Create buckets where INDEX = FREQUENCY
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # 3. Place numbers into their frequency bucket
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # 4. Read buckets from right to left (highest to lowest frequency)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]:  # Only iterate if the bucket has elements
                for num in buckets[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
                        
        return res