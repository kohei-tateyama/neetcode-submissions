class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range (0,len(nums)):
            j=i+1
            while j < len(nums):
                if nums[i] == nums[j]:
                    return True
                else:
                    j+=1
        return False
            