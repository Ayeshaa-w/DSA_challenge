class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        at,bt,ct=target
        found_a=False
        found_b=False
        found_c=False
        for a,b,c in triplets:
            if a>at or b>bt or c>ct :
                continue
            if a==at:found_a=True
            if b==bt:found_b=True
            if c==ct:found_c=True
            if found_a and found_b and found_c:
                return True
        return False

        