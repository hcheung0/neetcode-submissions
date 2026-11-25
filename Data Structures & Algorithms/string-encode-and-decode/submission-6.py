class Solution:

    def encode(self, strs: List[str]) -> str:
        
        # we add each string into a list, with a seperator and the legnth of each string

        encoded = []
        for string in strs:
            encoded.append(str(len(string))+":"+string)
        
        return "".join(encoded)


    def decode(self, s: str) -> List[str]:
        
        decode_list = []
        l, r = 0, 0

        while l < len(s):
            while s[r] != ":":
                r += 1
            length = int(s[l:r])
            decode_list.append(s[r+1:r+length+1])
        
            l = r+length+1
            r = l
        
        return decode_list
        
