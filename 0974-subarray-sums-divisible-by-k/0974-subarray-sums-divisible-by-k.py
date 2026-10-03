class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        freq=defaultdict(int)
        freq[0]=1
        prefix,count=0,0
        for num in nums:
            prefix+=num
            rem=prefix%k
            rem=(rem+k)%k
            if rem in freq:
                count+=freq[rem]
            freq[rem]+=1
        return count