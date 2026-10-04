class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char in hash_map:
                if not stack or stack[-1] != hash_map[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
