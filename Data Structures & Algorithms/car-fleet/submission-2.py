class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        has = {} 
        for i in range(len(position)):
            has.update({position[i] : speed[i] })
        position.sort()
        position.reverse()
        stack = []
        i = 0
        while i < len(position):
            if not stack:
                stack.append(i)
                i += 1
                continue
            curr = stack[-1]
            currSpeed = has.get(position[curr])
            curr = (target - position[curr]) / currSpeed
            nexSpeed = has.get(position[i])
            nex = (target - position[i]) / nexSpeed
            if nex <= curr:
                i += 1
                continue
                
            else:
                stack.append(i)
            i += 1 
        return len(stack)
            
            
        