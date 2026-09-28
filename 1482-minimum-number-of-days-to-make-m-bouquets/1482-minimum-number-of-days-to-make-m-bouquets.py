class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
                return -1
        def isvalid(mid,m,k,bloomDay):
            flowers,bouq=0,0
            for day in bloomDay:
                if day<=mid:
                    flowers+=1
                    if flowers==k:
                        bouq+=1
                        flowers=0
                else:
                    flowers=0
            return bouq>=m
        l,r=min(bloomDay),max(bloomDay)
        res=-1
        while l<=r:
            mid=l+((r-l)//2)
            if isvalid(mid,m,k,bloomDay):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
        