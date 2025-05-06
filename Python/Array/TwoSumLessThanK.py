class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        a = sorted(nums)
        i,j = 0 , len(a) - 1
        ans = -1
        while i < j:
            if a[i] + a[j] < k :
                ans = max(ans, a[i] + a[j])
                i +=1
            else:
                j -= 1
        return ans
        