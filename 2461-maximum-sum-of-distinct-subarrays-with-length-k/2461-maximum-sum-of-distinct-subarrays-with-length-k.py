class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = set()
        curr_sum = 0
        max_sum = 0
        l = 0

        for r in range(len(nums)):
            # 1. Instantly shrink window if a duplicate is found
            while nums[r] in seen:
                seen.remove(nums[l])
                curr_sum -= nums[l]
                l += 1

            # 2. Add current element to window
            seen.add(nums[r])
            curr_sum += nums[r]

            # 3. Shrink window if it exceeds length k
            if r - l + 1 > k:
                seen.remove(nums[l])
                curr_sum -= nums[l]
                l += 1

            # 4. Valid window of size k found
            if r - l + 1 == k:
                if curr_sum > max_sum:
                    max_sum = curr_sum

        return max_sum