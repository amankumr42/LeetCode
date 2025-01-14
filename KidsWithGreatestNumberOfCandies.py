class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        final_list = []
        max_val = max(candies)
        for candy in candies:
            if (max_val <=  (candy + extraCandies)):
                final_list.append(True)
            else:
                final_list.append(False)
        return final_list            
        