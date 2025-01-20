class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final_list = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == (nums[i] + nums[j]):
                    final_list.append(i)
                    final_list.append(j)
        return final_list
        