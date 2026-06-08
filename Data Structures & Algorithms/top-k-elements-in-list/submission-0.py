class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashTable = {}
        ans = []
        for num in nums:
            if hashTable.get(num) is None:
                hashTable.update({num:1})
            else:
                upd = hashTable.get(num) + 1
                hashTable[num] = upd
        valueTable = {}
        for num in range(len(nums) + 1):
            valueTable.update({num:[]})
        for num in hashTable:
            change = valueTable.get(hashTable[num])
            change.append(num)
            valueTable.update({hashTable[num]:change})
        i = len(valueTable) -1
        while len(ans) < k:
            for num in valueTable[i]:
                ans.append(num)
                if len(ans) >= k:
                    break
            i = i -1
        return ans





        


                
        