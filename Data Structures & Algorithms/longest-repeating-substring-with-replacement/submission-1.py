class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
       
        d = {}
        l = 0
        longest_window = 0

        for r in range(len(s)):
            if s[r] in d:
                d[s[r]] += 1
            else:
                d[s[r]] = 1

            max_frequency = max(d.values())
            
            if (r-l+1) - max_frequency > k:
                d[s[l]] -= 1
                l += 1
            
            current_window = r-l+1
            longest_window = max(longest_window, current_window)

        return longest_window
            


