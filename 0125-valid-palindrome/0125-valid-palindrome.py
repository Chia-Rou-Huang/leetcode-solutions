import re
class Solution:

    def isPalindrome(self, s: str) -> bool:
                s = re.sub(r'[^a-zA-Z0-9]', '', s)
                s=s.lower()
                x=len(s)
                m= x//2
                for i in range(m):
                    if s[i] != s[-i-1]:
                        return False
                return True
        