class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {'}' : '{', ')' : '(', ']' : '['}
        stack = []
        for p in s: 
            if p in closeToOpen:
                if not stack or closeToOpen[p] != stack.pop():
                    return False
            else:
                stack.append(p)
        return not stack