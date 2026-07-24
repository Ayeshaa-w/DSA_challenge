class Solution:
    def climbStairs(self, n: int) -> int:
        one,two=1,1 # two is also 1 becausee it sthe no of ways not the no of steps so from dtep last to raech last is 1 way by standing on the sae steop u cannot say 0 way s right
        for i in range(n-1):
            two,one=one,two+one
        return one
        