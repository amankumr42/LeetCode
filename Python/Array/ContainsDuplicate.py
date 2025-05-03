class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = False
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 0
            else:
                dict[num] = dict[num] + 1

        print(dict)
        for k,v in dict.items():
            val = dict.get(k)
            if val > 0 :
                res = True
                break
        return res
        
        