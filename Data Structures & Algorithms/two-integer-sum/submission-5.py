class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2: 
            return [0, 1]
        else: 
            dic = {key: index for index, key in enumerate(nums)}
            for i in range(len(nums)): 
                difference = target - nums[i]
                if difference in dic and dic[difference] != i: 
                    return [i, dic[difference]]