class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted = nums.sort()

        for i in range(0,len(nums)):
            j = int((len(nums) - i) / 2)
            while(j>i and j<=len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                elif nums[i] + nums[j] < target:
                    j = j + int((len(nums) - j)/2)
                else:
                    j = j - int((len(nums) - j)/2)

        