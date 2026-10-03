class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target=sum(nums)-x
        currsum=0
        l=0
        res=-1
        for r in range(len(nums)):
            currsum+=nums[r]
            while l<=r and currsum>target:
                currsum-=nums[l]
                l+=1
            if currsum==target:
                res=max(res,r-l+1)
        return len(nums)-res if res!=-1 else -1
                