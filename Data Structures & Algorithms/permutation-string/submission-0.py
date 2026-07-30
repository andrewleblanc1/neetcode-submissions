class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        i = 0
        j = 0
        count1  = [0] * 26
        count2  = [0] * 26
        for let in s1:
            val = ord(let) - 97 
            count1[val] += 1
        while j < len(s1):
            val = ord(s2[j]) - 97 
            count2[val] += 1
            j += 1
        if count1 == count2:
            return True
        while j < len(s2):
            val = ord(s2[i]) - 97 
            count2[val] -= 1
            i += 1
            val = ord(s2[j]) - 97 
            j += 1
            count2[val] += 1
            if count1 == count2:
                return True
        return False


        



        