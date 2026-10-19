class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Create dictionary
        # Sort every string in the list
        # Group strings together
        # ^ This was my initial solution. 
        # However, it is not the most efficient

        d1 = {}

        for string in strs:
            count = [0] * 26  # list of count for each of the 26 lowercase letters
            for char in string:
                index = ord(char) - ord('a')  # Takes ASCII key, takes "distance" from 'a'
                count[index] += 1 # count += 1
            
            key = tuple(count) # convert count into a tuple instead since lists aren't hashable

            if key in d1:
                d1[key].append(string) # if already present in d1, append
            else:
                d1[key] = [string] # if not present in d1, assign a list with it to d1
        
        return list(d1.values()) # return a list of only the values of d1

































