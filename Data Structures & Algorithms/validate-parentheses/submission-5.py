class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in pairs:
                if len(stack) == 0 or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

        
           
        


        