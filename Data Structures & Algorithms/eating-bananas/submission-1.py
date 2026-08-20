class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeConsumed(piles, k):
            time = 0
            for i in range(len(piles)): 
                time += math.ceil(piles[i]/k) 
            return time 
        
        lower, upper = 1, max(piles)
        res = upper 
        while lower <= upper: 
            mid = (lower + upper) // 2 
            if timeConsumed(piles, mid) <= h: 
                res = mid
                upper = mid - 1 
            else: 
                lower = mid + 1 
        return res
                