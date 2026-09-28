class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        l,r=0,0
        while l<=r and r<len(nums):
            while l<len(nums)  and nums[l]!=0:
                l+=1
            r=l+1
            while r<len(nums) and nums[r]==0 :
                r+=1
            if l<=r and r<len(nums):
                nums[l],nums[r]=nums[r],0
            
        """
        Do not return anything, modify nums in-place instead.
        """
        