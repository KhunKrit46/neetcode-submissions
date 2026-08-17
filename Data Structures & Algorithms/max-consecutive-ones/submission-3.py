class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxConsec = 0
        consec = 1
        check = nums[0]

        for i in range(1, len(nums)):
            if check == nums[i]:
                consec += 1
            else:
                if check == 1:
                    maxConsec = max(maxConsec, consec)

                consec = 1
                check = nums[i]

        # handle the final group
        if check == 1:
            maxConsec = max(maxConsec, consec)

        return maxConsec