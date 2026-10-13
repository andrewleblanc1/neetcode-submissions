class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        has = {}
        for let in s1:
            if has.get(let) is None:
                has.update({let: 1})
            else:
                curr = has.get(let)
                curr += 1
                has.update({let: curr})
        i, j = 0,0
        curr = {}
        while j < len(s2):
            if has.get(s2[j]) is None:
                j += 1
                i = j
                curr = {}
                continue
            if curr.get(s2[j]) is None:
                curr.update({s2[j]: 1})
            else:
                tot = curr.get(s2[j])
                tot += 1
                curr.update({s2[j]: tot})
            while i < j and curr.get(s2[j]) > has.get(s2[j]):
                tot = curr.get(s2[i])
                tot -= 1
                curr.update({s2[i]: tot})
                i += 1
            if curr == has:
                return True
            j += 1
        return False

            


        
        