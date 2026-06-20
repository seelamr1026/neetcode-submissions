class Solution:
    def isValid(self, s: str) -> bool:
        
        closed = [")","]","}"]
        opened = ["(","[","{"]
        
        stack = []

        for char in s:
            if char in closed and ( not stack or stack[-1] in closed):
                return False
            elif char in opened:
                stack.append(char)
            else:
                topVal = stack[-1]
                if (char == ")" and topVal == "(") or (char == "]" and topVal == "[") or (char == "}" and topVal == "{"):
                    stack = stack[:-1]
                else:
                    stack.append(char)
            
        return True if not stack else False
        