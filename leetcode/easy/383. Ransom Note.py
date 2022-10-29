from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = Counter(ransomNote)
        arr2 = Counter(magazine)
        for key in arr:
            if arr[key] > arr2[key]:
                return False
        return True
