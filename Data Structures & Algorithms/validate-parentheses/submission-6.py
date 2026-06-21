class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {'}' : '{', ')' : '(', ']' : '['}
        stack = []
        for p in s: 
            if p in closeToOpen and stack:
                if closeToOpen[p] != stack.pop():
                    return False
            else:
                stack.append(p)
        return len(stack) == 0