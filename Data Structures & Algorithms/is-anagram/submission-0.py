class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashTableOne = {}
        hashTableTwo = {}
        for i in s:
            if hashTableOne.get(i) == None:
                hashTableOne.update({i:1})
            else:
                curr = hashTableOne.get(i)
                curr += 1 
                hashTableOne.update({i: curr})
        for j in t:
            if hashTableTwo.get(j) == None:
                hashTableTwo.update({j:1})
            else:
                curr = hashTableTwo.get(j)
                curr += 1 
                hashTableTwo.update({j: curr})
        for i in s:
            if hashTableOne.get(i) != hashTableTwo.get(i):
                return False
        for j in t:
            if hashTableTwo.get(j) != hashTableOne.get(j):
                return False
        return True
        

        