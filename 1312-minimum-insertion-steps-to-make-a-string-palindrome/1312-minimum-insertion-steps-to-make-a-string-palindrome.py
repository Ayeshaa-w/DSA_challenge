class Solution:
    def minInsertions(self, s: str) -> int:
        def lcs(w1,w2):
            dp=[[0]*(len(w2)+1) for i in range(len(w1)+1)]
            for i in range(len(w1)-1,-1,-1):
                for j in range(len(w2)-1,-1,-1):
                    if w1[i]==w2[j]:
                        dp[i][j]=1+dp[i+1][j+1]
                    else:
                        dp[i][j]=max(dp[i+1][j],dp[i][j+1])
            return dp[0][0]
        rev_s=s[::-1]
        lps=lcs(s,rev_s)
        return len(s)-lps
        