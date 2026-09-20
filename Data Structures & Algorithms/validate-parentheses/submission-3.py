class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = {")":"(", "]":"[", "}":"{"}


        for char in s:
            if char in pairs.keys():
                if len(stack) == 0 or pairs[char] != stack[-1]:
                    return False
                stack.pop()
            elif char in pairs.values():
                stack.append(char)
        if len(stack) == 0:
            return True
        return False

        