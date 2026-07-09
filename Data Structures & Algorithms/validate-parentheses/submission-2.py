class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {")": "(", "]": "[", "}": "{"}
        arr = []

        for char in s:
            if char in hash_map:
                if len(arr) == 0 or arr.pop() != hash_map[char]:
                    return False
            else:
                arr.append(char)
        
        return len(arr) == 0