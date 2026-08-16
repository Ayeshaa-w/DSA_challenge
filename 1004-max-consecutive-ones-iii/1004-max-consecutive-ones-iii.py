class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,have=0,0
        max_len=0
        for r in range(len(nums)):
            if nums[r]==0:
                have+=1
            while have>k:
                if nums[l]==0:
                    have-=1
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len


        