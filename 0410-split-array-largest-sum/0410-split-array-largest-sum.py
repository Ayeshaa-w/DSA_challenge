class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r=max(nums),sum(nums)
        def cansplit(limit_mid):
            segments=0
            currnum=0
            for num in nums:
                currnum+=num
                if currnum>limit_mid:
                    segments+=1
                    currnum=num
            return segments+1<=k
        result=r
        while l<=r:
            mid=l+((r-l)//2)
            if cansplit(mid):
                result=mid
                r=mid-1
            else:
                l=mid+1
        return result
        