class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        S = {}
        T = {}
        for char in s:
            if char not in S:
                S[char] = 1
            else:
                S[char] += 1
        for char in t:
            if char not in T:
                T[char] = 1
            else:
                T[char] += 1
        for char in S:
            if char not in T or S[char] != T[char]:
                return False
        return True
        