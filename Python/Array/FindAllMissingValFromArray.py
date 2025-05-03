class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            index = abs(nums[i])-1
            nums[index] = -abs(nums[index])            
            
        return [index for index, n in enumerate(nums, start=1) if n > 0]