class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if sum(nums)<target:
            return 0
        l,currsum=0,0
        res=float('inf')
        for r in range(len(nums)):
            currsum+=nums[r]
            while currsum>=target and l<=r:
                res=min(res,r-l+1)
                currsum-=nums[l]
                l+=1
        return res