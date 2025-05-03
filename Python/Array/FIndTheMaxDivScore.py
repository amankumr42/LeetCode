class Solution:
    def maxDivScore(self, nums: List[int], divs: List[int]) -> int:
        return -max([sum(n % d == 0 for n in nums), -d] for d in divs)[1]