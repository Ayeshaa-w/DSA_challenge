class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        val=math.ceil(len(nums)/2)
        count=Counter(nums)
        for k,v in count.items():
            if v>=val:
                return k
                