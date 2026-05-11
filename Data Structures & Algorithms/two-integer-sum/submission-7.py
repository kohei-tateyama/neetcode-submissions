class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indeces = {}

        for i, num in enumerate(nums):
            indeces[num] = i
        
        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff in indeces and indeces[diff] != i:
                return [min(i,indeces[diff]), max(i,indeces[diff])]
        return []