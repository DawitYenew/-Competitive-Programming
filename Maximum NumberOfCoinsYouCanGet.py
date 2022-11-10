class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        me = len(piles)-2
        bob = 0
        alice = len(piles) - 1
        total = 0
        while bob < me:
            total += piles[me]
            me -= 2
            bob += 1
        return total
