class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        else:
            if needle in haystack:
                for i in range (len(needle), len(haystack) + 1):
                    if  haystack[i-len(needle):i] == needle:
                        return i-len(needle)
            else:
                return -1
        