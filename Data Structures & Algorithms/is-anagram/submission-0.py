class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ds = {}
        dt = {}

        for letter in s:
            if letter in ds:
                ds[letter] = ds[letter] + 1
            else:
                ds[letter] = 1

        for letter in t:
            if letter in dt:
                dt[letter] = dt[letter] + 1
            else:
                dt[letter] = 1

        return dt == ds
        