class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = -1
        has = {}
        ans = 0
        for r in range(len(s)):
            if has.get(s[r]) == None:
                has.update({s[r]:1})
            else:
                new = has.get(s[r])
                new += 1
                has.update({s[r]:new})
            tot = 0
            m = 0
            for x in has:
                tot += has[x]
                m = max(has[x], m)
            tot = tot - m
            while tot > k:
                l += 1
                let = has.get(s[l])
                let -= 1
                has.update({s[l]:let})
                tot = 0
                m = 0
                for x in has:
                    tot += has[x]
                    m = max(has[x], m)
                tot = tot - m
            ans = max(ans, r - l)
        return ans

            


    

        
        
        