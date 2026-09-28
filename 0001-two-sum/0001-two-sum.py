class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i,val in enumerate(nums):
            diff=(target-val)
            print(diff)
            if diff not in seen:
                seen[val]=i
            else:
                return [seen[diff],i] 

        