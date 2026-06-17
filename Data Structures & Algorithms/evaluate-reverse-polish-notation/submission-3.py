class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for operation in tokens:
            if operation == '+':
                stack.append(stack.pop() + stack.pop())
            elif operation == '*':
                stack.append(stack.pop() * stack.pop())
            elif operation == '/':
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            elif operation == '-':
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            else:
                stack.append(int(operation))
        return stack[0]