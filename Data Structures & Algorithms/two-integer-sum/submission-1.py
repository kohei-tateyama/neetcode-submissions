class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A=[]
        for i, num in enumerate(nums):
            A.append([i,num])

        i,j = 0,len(nums)-1
        while(i<j):
            total = A[i][1] + A[j][1]
            if total == target:
                return [min(A[i][0],A[j][0]), max(A[i][0],A[j][0])]        
            elif total < target:
                i+=1
            else:
                j-=1
        return[]