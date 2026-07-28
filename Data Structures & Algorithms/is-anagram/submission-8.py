class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        D = {}
        for char in s:
            if char not in D:
                D[char] = 1
            else:
                D[char] += 1
        for char in t:
            if char not in D:
                return False
            else:
                D[char] -= 1
        for char in D:
            if D[char] != 0:
                return False
        return True

        