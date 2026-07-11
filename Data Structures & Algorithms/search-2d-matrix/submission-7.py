class Solution:
    def binarySearch(self, arr: List[int], target: int) -> bool:
        l = 0
        r = len(arr) - 1
        m = (r-l) // 2
        while l <= r:
            print("binary search")
            print(l)
            print(r)    
            if target == arr[m]:
                return True
            elif target > arr[m]:
                l = m + 1
                m = ((r - l) // 2) + l
            elif target < arr[m]:
                r = m - 1
                m = ((r-l) // 2) + l
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        m = (r-l) // 2
        while l <= r:
            print("matrix search)")
            print(l)
            print(r)
            if target >= matrix[m][0] and target <= matrix[m][(len(matrix[m])-1)]:
                if self.binarySearch(matrix[m], target) == True:
                    return True
                else:
                    return False
            elif target < matrix[m][0]:
                r = m - 1
                m = ((r-l) // 2) + l
            elif target > matrix[m][(len(matrix[m])-1)]:
                l = m + 1
                m = ((r-l) // 2) + l
        return False