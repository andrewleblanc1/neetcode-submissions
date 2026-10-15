class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char for char in s if char.isalnum())
        cleanedLower = cleaned.lower()
        l ,r = 0, len(cleaned) -1
        while l < r:
            if cleanedLower[l] != cleanedLower[r]:
                return False
            l += 1
            r -= 1
        return True
        