class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        
        count = Counter(s)  # Hitung frekuensi tiap karakter
        
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        
        return -1
