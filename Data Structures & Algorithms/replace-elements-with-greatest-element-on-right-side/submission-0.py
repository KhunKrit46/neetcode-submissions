class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        check = 0
        for i in range(len(arr)): 
            if i == 0: 
                check = arr[len(arr)-i-1]
                arr[len(arr)-i-1] = -1
            else: 
                if arr[len(arr)-i-1] <= check: 
                    arr[len(arr)-i-1] = check
                else: 
                    newCheck = arr[len(arr)-i-1]
                    arr[len(arr)-i-1] = check
                    check = newCheck
        return arr