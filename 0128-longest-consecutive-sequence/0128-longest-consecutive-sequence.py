class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        max_len=0
        if not nums:
            return max_len
        count=set(nums)
        for num in count:
            if num-1 not in count:
                curr=num
                currlen=1
                while (curr+1) in count:
                    curr+=1
                    currlen+=1
                max_len=max(max_len,currlen)
        return max_len