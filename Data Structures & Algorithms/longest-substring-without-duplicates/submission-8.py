class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set({})
        length = 0
        l = 0
        for r in range(len(s)):
            while s[r] in myset:
                myset.remove(s[l])
                l += 1
            myset.add(s[r])
            length = max(length, r - l + 1)
        return length


            


        