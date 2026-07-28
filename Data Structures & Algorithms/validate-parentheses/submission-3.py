class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ref = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for char in s:
            if char in ref:
                stack.append(char)
            elif stack and ref[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return not stack
