import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        clean_paragraph = re.sub(r'[^\w\s]', ' ', paragraph).lower()
        
        words = clean_paragraph.split()

        banned_set = set(banned)

        counts = {}
        for w in words:
            if w not in banned_set:
                counts[w] = counts.get(w, 0) + 1
        
        return max(counts, key=counts.get)