class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        set_j = set(list(jewels))

        count = 0
        for l in list(stones):
            if l in set_j:
                count+=1

        return(count)
