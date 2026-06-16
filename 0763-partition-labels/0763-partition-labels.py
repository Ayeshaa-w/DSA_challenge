class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count=Counter(s)
        total=0
        res=[]
        q=deque()
        seen=set()
        for char in s:
            count[char]-=1
            total+=1
            if char not in seen:
                seen.add(char)
                q.append(char)
            while q and count[q[0]]==0:
                q.popleft()
            if not q:
                res.append(total)
                total=0
        return res
        