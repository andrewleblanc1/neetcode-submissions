class Solution:

    def encode(self, strs: List[str]) -> str:
        secret = ""
        for word in strs:
            secret = secret + "#" + str(len(word))  + "#" + word
        return secret
            

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            length = ""
            if s[i] == "#":
                i += 1
                while s[i] != "#":
                    length = length + s[i]
                    i += 1
                print(length)
                length = int(length)
                
                ans.append(s[(i + 1) : (i + 1 + length)])
                i = i + 1 + length
        return ans
    


                



