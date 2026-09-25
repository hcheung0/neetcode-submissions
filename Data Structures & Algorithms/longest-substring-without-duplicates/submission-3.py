class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        characters = {}
        l, r = 0, 0
        longest = 0
        

        while r != len(s):
            if s[r] not in characters or characters[s[r]] < l:
                characters[s[r]] = r
                r += 1
            else:
                l = characters[s[r]] + 1
                characters[s[r]] = r
                r += 1
            if len(s[l:r]) >= longest:
                longest = len(s[l:r])


        return longest


 

