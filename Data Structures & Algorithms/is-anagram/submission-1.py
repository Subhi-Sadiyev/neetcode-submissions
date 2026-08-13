class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frequency1 = {}
        frequency2 = {}
        for char in s:
            frequency1[char] = frequency1.get(char, 0) + 1
        for char in t:
            frequency2[char] = frequency2.get(char, 0) + 1
        return frequency1 == frequency2
