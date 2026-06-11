class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            p1 = i
            p2 = len(numbers) - 1
            while p1 != p2:
                if (numbers[p1] + numbers[p2]) == target:
                    ans = []
                    p1 +=1
                    p2 +=1
                    ans.append(p1)
                    ans.append(p2)
                    return ans
                p2 -= 1



        