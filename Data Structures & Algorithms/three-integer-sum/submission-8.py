class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()
        for i in range(len(nums)): 
            if nums[i] > 0: #positive only
                break
            if nums[i] == nums[i-1] and i > 0: 
                continue
            j, k = i+1, len(nums)-1 
            target = nums[i]
            while j < k: 
                if nums[i] + nums[j] + nums[k] == 0: 
                    sol.append([nums[i], nums[j], nums[k]])
                    j = j+1
                    k = k - 1 
                    while j < k and nums[j] == nums[j-1]: 
                        j += 1 
                elif nums[i] + nums[j] + nums[k] < 0:
                    j = j + 1  
                else: 
                    k = k - 1 
        return sol
            

        