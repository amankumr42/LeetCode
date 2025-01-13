from math import gcd

class Solution:
    def gcdOfStrings(self, A: str, B: str) -> str:
        # Check if the strings can form a valid pattern
        if A + B != B + A:
            return ""
        # Use the GCD of the lengths of A and B to find the GCD string
        gcd_length = gcd(len(A), len(B))
        return A[:gcd_length]
        