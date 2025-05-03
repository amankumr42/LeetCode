class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit_str = "".join(map(str, digits))
        print(digit_str)
        num = int(digit_str) + 1
        return list(map(int, str(num) ))
