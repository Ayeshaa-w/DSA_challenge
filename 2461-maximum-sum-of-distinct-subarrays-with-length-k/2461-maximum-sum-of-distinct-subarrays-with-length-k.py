class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l,max_sum,curr_sum=0,0,0
        count=defaultdict(int)
        for r in range(len(nums)):
            curr_sum+=nums[r]
            count[nums[r]]+=1
            if r-l+1>k:
                count[nums[l]]-=1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                curr_sum-=nums[l]
                l+=1
            if r-l+1==k and len(count)==k:
                max_sum=max(max_sum,curr_sum)
        return max_sum