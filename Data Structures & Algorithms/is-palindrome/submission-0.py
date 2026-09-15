class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        a = ""
        for letter in s:
            if letter.isalnum():
                a += letter
        
        for i, letter in enumerate(a):
            if letter.lower() != a[len(a)-(i+1)].lower():
                return False
        return True
