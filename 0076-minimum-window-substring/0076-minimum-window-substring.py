class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count={}
        window={}
        have,l=0,0
        string=""
        min_len=float('inf')
        for i in range(len(t)):
            count[t[i]]=1+count.get(t[i],0)
        need=len(count)
        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)
            if c in count and window[c]==count[c]:
                have+=1
                print(f"have:{have}")
            while have==need:
                if (r-l+1)<min_len:
                    min_len=(r-l+1)
                    string=s[l:r+1]
                window[s[l]]-=1
                if s[l] in count and window[s[l]]<count[s[l]]:
                    have-=1
                l+=1
        return string 
        
        