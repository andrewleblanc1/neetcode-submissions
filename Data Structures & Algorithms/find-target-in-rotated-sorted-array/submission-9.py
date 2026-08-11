class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        l = 0
        r = len(nums) - 1



        while l < r:
            m = ((r - l) // 2) + l
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        m = ((r - l) // 2) + l
        split = m

        list1 = nums[0:l]
        list2 = nums[l:]
        l1 = 0
        r1 = len(list1) - 1
        if len(list1) != 0:
            while l1 < r1:
                m1 = ((r1 - l1) // 2) + l1
                if list1[m1] == target:
                    return m1
                elif list1[m1] > target:
                    r1 = m1 - 1
                else:
                    l1 = m1 + 1
            m1 = ((r1 - l1) // 2) + l1
            if list1[m1] == target:
                return m1
        l2 = 0
        r2 = len(list2) - 1
        if len(list2) != 0:
            while l2 < r2:
                m2 = ((r2 - l2) // 2) + l2
                print(list2[m2])
                if list2[m2] == target:
                    return m2 + split
                elif list2[m2] > target:
                    r2 = m2 - 1
                else:
                    l2 = m2 + 1
            m2 = ((r2 - l2) // 2) + l2
            if list2[m2] == target:
                return m2 + split
        return -1
        


        
                    
        
            

            

        


       
        
        