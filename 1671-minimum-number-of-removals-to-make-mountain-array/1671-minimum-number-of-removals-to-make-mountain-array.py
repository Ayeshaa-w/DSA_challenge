class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        lis=[1]*len(nums)
        lds=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    lis[i]=max(lis[i],1+lis[j])
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    lds[i]=max(lds[i],1+lds[j])
        res=len(nums)
        for i in range(len(nums)):
            if lis[i]>1 and lds[i]>1:
                res=min(res,len(nums)-lis[i]-lds[i]+1)
        return res






        
        