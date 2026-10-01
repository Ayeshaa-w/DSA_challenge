class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix,ans=0,0
        freq={0:-1}
        for i,num in enumerate(nums):
            if num==0:
                prefix+=-1
            else:
                prefix+=1
            if prefix in freq:
                ans=max(ans,i-freq[prefix])
            else:
                freq[prefix]=i
        return ans