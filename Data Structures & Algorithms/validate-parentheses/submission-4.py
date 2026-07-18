class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 0:
            return True
        elif len(s)%2 != 0:
            return False
        
        stack = []
        openPar = ["(","[","{"]
        closedPar = [")","]","}"]

        for char in s:
            if char in openPar:
                stack.append(char)
            if char in closedPar:
                if len(stack) == 0:
                    return False
                if (char == ")" and stack[-1] == "(") or (char == "]" and stack[-1] == "[") or (char == "}" and stack[-1] == "{"):
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False


        