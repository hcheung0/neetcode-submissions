class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Create dictionary
        # Sort every string in the list
        # Group strings together
        # ^ This was my initial solution. 
        # However, it is not the most efficient

        d1 = {}

        for string in strs:
            # create an array of all 26 letters
            letters = [0] * 26

            for char in string:
                value = ord(char) - ord('a') # had this in reverse
                letters[value] += 1
            
            key = tuple(letters)

            if key in d1:
                d1[key].append(string) # did += 1 instead (should reread problem in future)
            else:
                d1[key] = [string] # did = 1 instead (same as above)
            
        
        return list(d1.values()) # returned entire dictionary rather than only values 

































