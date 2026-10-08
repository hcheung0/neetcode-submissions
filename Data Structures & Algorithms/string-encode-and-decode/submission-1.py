class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_list = []
        for string in strs:
            encoded_list.append(str(len(string)) + ":" + string)

        return "".join(encoded_list)

    def decode(self, s: str) -> List[str]:

        i, j = 0, 0
        decode_list = []

        while i < len(s):
            while s[j] != ":":
                j += 1
            length = int(s[i:j])
            decode = s[j+1:j+length+1]
            decode_list.append(decode)
           
            i = j+length+1
            j = i

        return decode_list 


