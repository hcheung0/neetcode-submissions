class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create dictionaries for each set of anagrams

        d1 = {}

        for string in strs:
            new_string = "".join(sorted(string));
            if new_string in d1:
                d1[new_string].append(string)
            else:
                d1[new_string] = [string]
        
        return list(d1.values())


