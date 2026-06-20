class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for char in tokens:
            val = 0
            if char not in ("+", "-", "*", "/"):
                stack.append(char)
            else:
                print(stack)
                a= int(stack.pop())
                b= int(stack.pop())
                #stack = stack[:-2]
                if char == "+":
                    val = b+a
                elif char == "-":
                    val = b-a
                elif char == "*":
                    val = a*b
                else:
                    val = b/a
                stack.append(str(int(val)))
        
        return int(stack[-1])
                