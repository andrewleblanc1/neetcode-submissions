class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for st in s:
            if not stack:
                stack.append(st)
                continue
            curr = stack[-1]
            if ord(curr) == 40:
                if ord(st) == 41:
                    stack.pop()
                else:
                    stack.append(st)
            else:
                if ord(st) == (ord(curr) + 2):
                    stack.pop()
                else:
                    stack.append(st)
            
        if len(stack) == 0:
            return True
        else:
            return False
        
        