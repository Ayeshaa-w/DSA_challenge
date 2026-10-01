class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        prefix=[0]*(n+2)
        for i,r,val in bookings:
            prefix[i]+=val
            prefix[r+1]-=val
        res=[]
        currsum=0
        for num in prefix[1:len(prefix)-1]:
            currsum+=num
            res.append(currsum)
        return res
