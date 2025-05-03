class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        res = None
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] = freq[num] + 1
        for k in freq.keys():
            val = freq[k]
            if val == 1:
                res = k
        return res
