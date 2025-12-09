class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(":")","[":"]","{":"}"}

        for char in s:
            if char in mapping:
                stack.append(char)

            else:
                                
                if not stack:
                    return False

                last_char = stack.pop()

                if mapping[last_char] != char:
                    return False
                
        return len(stack) == 0

