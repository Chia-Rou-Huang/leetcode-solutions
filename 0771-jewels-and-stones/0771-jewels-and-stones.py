class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        list=[]
        for i in range (len(stones)):
            if stones[i]in jewels:
                list.append(stones[i])
        return len(list)