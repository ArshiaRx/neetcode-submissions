class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
         
        # create a list
        stack = []

        for char in tokens:
            
            # simply check the conditions and pop and add them up into the stack list
            if char == "+":
                stack.append(stack.pop() + stack.pop())

            elif char == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            elif char == "*":
                stack.append(stack.pop() *  stack.pop())

            elif char == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))

            else:
                stack.append(int(char))
        return stack[0]