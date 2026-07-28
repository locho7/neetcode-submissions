class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            lc = s[l].lower()
            rc = s[r].lower()
            if not (lc.isalpha() or lc.isnumeric()):
                l += 1
                continue
            if not (rc.isalpha() or rc.isnumeric()):
                r -= 1
                continue
        
            print(f"test: {lc}, {rc}")
            if lc != rc:
                return False
            l += 1
            r -= 1
        return True
            

