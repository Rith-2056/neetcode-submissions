class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = "".join(ch.lower() for ch in s if ch.isalnum())
        left = 0
        right = len(sentence) - 1
        while left < right:
            if sentence[left] != sentence[right]:
                return False
            left += 1
            right -= 1
        return True