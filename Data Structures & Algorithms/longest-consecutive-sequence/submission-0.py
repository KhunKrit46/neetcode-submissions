class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        if len(numset) == 0:
            return 0
        if len(numset) == 1:
            return 1

        smallest = min(numset)
        longest = 1
        streak = 1
        curr = smallest
        numset.remove(smallest)
        while numset:
            print(curr)
            if (curr + 1) in numset:
                streak += 1
                numset.remove(curr + 1)
                curr = curr + 1
            else:
                longest = streak if streak > longest else longest
                streak = 1
                curr = min(numset)
                numset.remove(curr)
        longest = streak if streak > longest else longest
        return longest
                
