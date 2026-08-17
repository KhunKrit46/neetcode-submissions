class Solution:
    def isValid(self, s: str) -> bool:
        validStack = []
        validStack.append(s[0])
        for i in range(1,len(s)):
            if s[i] in ["]", ")", "}"]:
                if not validStack:
                    return False
                else:
                    if s[i] == ")":
                        if validStack[-1] == "(":
                            validStack.pop()
                        else: return False
                    elif s[i] == "]":
                        if validStack[-1] == "[":
                            validStack.pop()
                        else: return False
                    elif s[i] == "}":
                        if validStack[-1] == "{":
                            validStack.pop()   
                        else: return False
            else: 
                validStack.append(s[i])      
        if validStack: 
            return False 
        else: 
            return True