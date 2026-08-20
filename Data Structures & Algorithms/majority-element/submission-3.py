class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # return max(Counter(nums), key = Counter(nums).get)
        # above is O(n) space next one is O(1) space
        candidate = nums[0]
        cnt = 0 
        for num in nums:
            if num == candidate: 
                cnt += 1 
            else: 
                cnt -= 1 
                if cnt < 0: 
                    candidate = num
                    cnt = 1 
        return candidate