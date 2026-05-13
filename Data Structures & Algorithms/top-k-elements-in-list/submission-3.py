class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in range(0, len(nums)):
            if nums[i] not in counts:
                counts[nums[i]] = 1
            else:
                counts[nums[i]] += 1
        
        sorted_counts = sorted(counts.keys(), key = lambda x: counts[x], reverse = True)
        return sorted_counts[:k]