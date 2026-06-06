class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashTable = {}
        for num in nums:
            if hashTable.get(num) != None:
                return True
            hashTable[num] = "true"
        return False
        