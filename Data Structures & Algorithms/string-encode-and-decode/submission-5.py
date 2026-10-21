class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_list = []
        for string in strs:
            encoded_list.append(str(len(string)) + ":" + string)   # Supposed to add delimiter here not after
        
        encoded_list = "".join(encoded_list) # You cant do this because it wont allow length information
        print(encoded_list)

        return encoded_list


    def decode(self, s: str) -> List[str]:
        
        decode_list = []
        l, r = 0, 0

        '''
        for i, char in enumerate(s):  # Entirely different loop structure
            if char == "&":
                length = int(i-1)
                decoded_list.append(s[l+1:r+1])
                l = r
        '''

        while l < len(s):
            while s[r] != ":":
                r += 1
            length = int(s[l:r])
            decode_list.append(s[r+1:r+length+1])

            l = r+length+1
            r = l
        
        
        print(decode_list)
        return decode_list
       


