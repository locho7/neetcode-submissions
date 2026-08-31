class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longestLen = 0
        substr = {}

        for i in range(len(s)):
            if s[i] not in substr:
                substr[s[i]] = i
            else:
                j = substr[s[i]]
                substr[s[i]] = i
                if j >= l:
                    l = j + 1
                    r = i
            r += 1
            longestLen = max(r - l, longestLen)

        return longestLen
                
