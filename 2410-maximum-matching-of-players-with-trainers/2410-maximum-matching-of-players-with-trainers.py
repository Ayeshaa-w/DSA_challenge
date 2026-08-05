class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players=sorted(players)
        trainers=sorted(trainers)
        l,r=0,0
        while r<len(trainers) and l<len(players):
            if trainers[r]>=players[l]:
                l+=1
            r+=1
        return l
        