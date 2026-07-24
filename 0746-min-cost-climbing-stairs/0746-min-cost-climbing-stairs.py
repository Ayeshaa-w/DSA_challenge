class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        one,two=cost[n-1],0
        for i in range(n-2,-1,-1):
            temp=one
            one=min(cost[i]+one,cost[i]+two)
            print(one)
            two=temp
            print(two)
        return min(one,two)
        