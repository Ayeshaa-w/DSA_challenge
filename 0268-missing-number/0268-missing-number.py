class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums=set(nums)
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i
            
