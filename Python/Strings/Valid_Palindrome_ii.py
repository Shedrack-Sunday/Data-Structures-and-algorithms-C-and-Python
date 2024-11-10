
class Solution:
    def helper(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return self.helper(s, i, j - 1) or self.helper(s, i + 1, j)
            i += 1
            j -= 1
        return True
         







        
