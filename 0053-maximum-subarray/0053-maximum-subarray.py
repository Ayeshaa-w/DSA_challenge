class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum=0
        res=float('-inf')
        for num in nums:
            currsum+=num
            res=max(res,currsum)
            if currsum<0:
                currsum=0
        return res
        