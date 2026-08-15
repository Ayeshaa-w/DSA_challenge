class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        count=defaultdict(int)
        l=0
        curr_sum,max_sum=0,0
        for r in range(len(nums)):
            if l<=r and r-l>k-1:
                max_sum=max(max_sum,curr_sum)
                count[nums[l]]-=1
                curr_sum-=nums[l]
                l+=1
            while l<=r and count[nums[r]]>=1:
                count[nums[l]]-=1
                curr_sum-=nums[l]
                l+=1
            
            curr_sum+=nums[r]
            count[nums[r]]+=1
        if r-l+1>=k:
            max_sum=max(max_sum,curr_sum)
        return max_sum
            


        