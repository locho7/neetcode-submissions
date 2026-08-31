class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longestLen = 0
        substr = {}

        for i in range(len(s)):
            if s[i] not in substr:
                substr[s[i]] = i
                r += 1
            else:
                j = substr[s[i]]
                substr[s[i]] = i
                if j >= l:
                    longestLen = max(r - l, longestLen)
                    l = j + 1
                    r = i + 1
                    substr[s[i]] = i

                    if len(s) - l < longestLen:
                        return longestLen
                else:
                    r += 1
            longestLen = max(r - l, longestLen)

        return longestLen
                
