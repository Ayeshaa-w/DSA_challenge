class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g=sorted(g,reverse=True)
        s=sorted(s,reverse=True)
        l,r,count=0,0,0
        while r<len(s) and l<len(g):
            if g[l]<=s[r]:
                count+=1
                r+=1
            l+=1
        return count
        