from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        freq =  [[] for i in range(len(nums) + 1)]
        for f in freqMap: 
            freq[freqMap[f]].append(f)
        res = []
        for i in range(len(freq)-1, 0, -1): 
            if freq[i]: 
                res += freq[i]
                if len(res) == k: 
                    return res
            
        