class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeConsumed(arr, n): 
            time = 0 
            for a in arr: 
                time += math.ceil(a/n)
            return time
        upper = max(piles)
        lower = 1

        ans = upper

        while lower <= upper: 
            mid = (lower + upper) // 2 
            if timeConsumed(piles, mid) <= h: 
                ans =  mid
                upper = mid - 1 
            else: 
                lower = mid + 1 
        return ans



                