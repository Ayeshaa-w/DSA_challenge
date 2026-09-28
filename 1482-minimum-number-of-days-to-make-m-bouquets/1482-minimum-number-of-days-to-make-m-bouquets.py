class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        def isvalid(mid,m,k,bloomDay):
            boolean=[False]*len(bloomDay)
            for i in range(len(bloomDay)):
                if bloomDay[i]<=mid:
                    boolean[i]=True
            flowers,bouq=0,0
            for bloomed in boolean:
                if bloomed:
                    flowers+=1
                    if flowers==k:
                        bouq+=1
                        flowers=0
                else:
                    flowers=0
            return bouq>=m
        l,r=1,max(bloomDay)
        res=-1
        while l<=r:
            mid=l+((r-l)//2)
            if isvalid(mid,m,k,bloomDay):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
        