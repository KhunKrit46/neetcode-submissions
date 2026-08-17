class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new = 0
        newL = []

        for i in range(len(nums)):
            if nums[i] != val:
                new += 1
                newL.append(nums[i])

        nums[:] = newL
        return new