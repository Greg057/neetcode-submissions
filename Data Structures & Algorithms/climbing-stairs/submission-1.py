class Solution:
    def climbStairs(self, n: int) -> int:
        phi = (1 + 5 ** 0.5) / 2
        return int((phi ** (n + 1) - (1 - phi) ** (n + 1)) / (5 ** 0.5))