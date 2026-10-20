class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for s in strs:
            curr = len(s)
            encoding += (str(curr) + "#")
            encoding += s
        return encoding


    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            curr = ""
            length = ""
            j = 0
            while s[j] != "#":
                length += s[j]
                j += 1
            length = int(length)
            for i in range(j + 1, length + j + 1):
                curr += s[i]
            res.append(curr)
            if (length + j + 1) >= len(s):
                break
            s = s[(length + j + 1):]
        return res
