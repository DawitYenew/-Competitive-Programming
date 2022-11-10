class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        st, r = 0, len(cardPoints) - k
        if k > len(cardPoints): return 0
        sums = sum(cardPoints[r:])
        max_result = sums

        while r < len(cardPoints):
            sums += (cardPoints[st] - cardPoints[r])
            max_result = max(max_result, sums)
            st += 1
            r+=1
        
        return max_result

