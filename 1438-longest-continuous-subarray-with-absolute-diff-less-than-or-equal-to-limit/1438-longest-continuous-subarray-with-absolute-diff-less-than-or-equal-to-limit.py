class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        dq1,dq2=collections.deque(),collections.deque()
        res=float('-inf')
        l=0
        for r in range(len(nums)):
            while dq1 and nums[dq1[-1]]<=nums[r]:
                dq1.pop()
            while dq2 and nums[dq2[-1]]>=nums[r]:
                dq2.pop()
            dq1.append(r)
            dq2.append(r)
            while nums[dq1[0]]-nums[dq2[0]]>limit:
                if l==dq1[0]:
                    dq1.popleft()
                if l==dq2[0]:
                    dq2.popleft()
                l+=1
            res=max(res,r-l+1)
        return res