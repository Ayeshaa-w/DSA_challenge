class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p)>len(s):
            return []
        counts=[0]*26
        countp=[0]*26
        res=[]
        for i in range(len(p)):
            counts[ord(s[i])-ord('a')]+=1
            countp[ord(p[i])-ord('a')]+=1
        if counts==countp:
            res.append(0)
        l=0
        for i in range(len(p),len(s)):
            counts[ord(s[i])-ord('a')]+=1
            counts[ord(s[l])-ord('a')]-=1
            l+=1
            if counts==countp:
                res.append(l)
        return res
