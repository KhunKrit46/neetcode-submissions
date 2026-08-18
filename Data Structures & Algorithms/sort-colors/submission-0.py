class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0,0,0]
        for num in nums: 
            if num == 0: 
                freq[0] += 1 
            elif num == 1: 
                freq[1] += 1
            else: 
                freq[2] += 1 
        i = 0 
        for x in range(len(freq)): 
            for n in range(freq[x]): 
                nums[i] = x
                i += 1 
        return nums