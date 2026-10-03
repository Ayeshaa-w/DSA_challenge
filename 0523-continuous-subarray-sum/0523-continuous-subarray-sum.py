class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        first={0:-1}#storage of index
        prefix=0
        for i,num in enumerate(nums):
            prefix+=num
            rem=prefix%k
            rem=(rem+k)%k
            if rem in first:
                if (i-first[rem])>1:
                    return True
            else:
                first[rem]=i
        return False