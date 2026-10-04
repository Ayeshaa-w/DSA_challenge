class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l,have,res=0,0,0
        for r in range(len(nums)):
            if nums[r]==0:
                have+=1
            while have>k:
                if nums[l]==0:
                    have-=1
                l+=1
            res=max(res,r-l+1)
        return res