class Solution:
    def reverseWords(self, s: str) -> str:
        final_list = []
        temp_list = []
        str_list = s.split(" ")
        print(str_list)
        for i in str_list:
            if i != "":
                temp_list.append(i)
        temp_list.reverse()
        print(temp_list)
        res = " ".join(temp_list)
        print(res)        
        return res
