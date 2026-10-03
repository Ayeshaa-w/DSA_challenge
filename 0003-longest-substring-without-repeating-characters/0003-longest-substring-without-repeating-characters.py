class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        fmap={}
        res=0
        for i in range(len(s)):
            if s[i] in fmap and fmap[s[i]]>=l:
                l=fmap[s[i]]+1
            res=max(res,i-l+1)
            fmap[s[i]]=i
        return res