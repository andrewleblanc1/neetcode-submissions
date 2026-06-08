class Solution:
    def isAnagram(self, a: str, b: str):
        if len(a) != len(b):
            return False
        count = [0] * 26
        for i in range(len(a)):
            count[ord(a[i]) - ord('a')] += 1
        for j in range(len(b)):
            count[ord(b[j]) - ord('a')] += -1
        for num in count:
            if num != 0:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        check = True
        for st in strs:
            check = True
            if len(ans) == 0:
                ans.append([st])
            else:
                for a in ans:
                    if self.isAnagram(a[0],st):
                        a.append(st)
                        check = False
                        break
                if check:
                    ans.append([st])
        return ans