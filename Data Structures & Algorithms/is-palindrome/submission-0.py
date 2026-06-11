class Solution:
    def collapseStr(self, s:str) -> str:
        ans = s.lower()
        ans = ''.join(c for c in ans if c.isalnum())
        return ans

    def isPalindrome(self, s: str) -> bool:
        s = self.collapseStr(s)
        ind = len(s) // 2 
        for i in range(0,(ind)):

            if s[i] != s[len(s) - 1 - i]:
                return False
        #if (len(s) % 2) == 1:
          #  ind = len(s) // 2 
          #  for i in range(0,(ind)):
          #      if s[i] != s[len(s) - 1 - i]:
          #          return False
       # else:
          #  for i in range(0,(ind - 1)):
          #      if s[i] != s[len(s) - 1 - i]:
           #         return False
        return True

                    



        