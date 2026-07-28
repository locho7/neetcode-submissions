class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        i = 0
        l = len(s)
        while i < l:
            char = s[i]
            print(s)
            if (not char.isalpha()) and (not char.isdigit()):
                s = s[:i] if i + 1 == len(s) else s[:i] + s[i+1:]
                l = len(s)
            i += 1
        
        for i in range(len(s)//2):
            left = s[i]
            right = s[-i-1]
            if left != right: return False
        
        return True

