class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        mapping = {')': '(', '}': '{', ']': '['}
        if len(s)<=1:
            return False
        for char in s:
         if char in mapping.values():
            stack.append(char)
         elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
        if not stack:
             return True
