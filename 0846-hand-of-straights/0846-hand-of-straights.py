class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        n=len(hand)//groupSize #no of groups to be formed
        hand=sorted(hand) #sort the ip
        arr=[[] for _ in range(n)] #[[],[],[]]
        for h in hand:
            placed=False
            for j in range(n):
                if (len(arr[j])>0 and len(arr[j])<groupSize and arr[j][-1]+1==h):
                    arr[j].append(h)
                    placed=True
                    break
            if not placed:
                for j in range(n):
                    if len(arr[j])==0:
                        arr[j].append(h)
                        placed=True
                        break
            if not placed:
                return False
        return True
        