class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Create dictionary
        # Sort every string in the list
        # Group strings together
        # ^ This was my initial solution. 
        # However, it is not the most efficient

        d1 = {}

        for string in strs:
            count = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                count[index] += 1
            
            key = tuple(count)

            if key in d1:
                d1[key].append(string)
            else:
                d1[key] = [string]
        
        return list(d1.values())

































