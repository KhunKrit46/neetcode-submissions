class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        check = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-1): 
            if arr[len(arr)-i-2] <= check: 
                arr[len(arr)-i-2] = check
            else: 
                newCheck = arr[len(arr)-i-2]
                arr[len(arr)-i-2] = check
                check = newCheck
        return arr