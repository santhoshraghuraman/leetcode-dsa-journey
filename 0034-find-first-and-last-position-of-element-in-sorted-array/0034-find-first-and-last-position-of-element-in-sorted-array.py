class Solution:
    def searchRange(self, nums, target):

        first = -1
        left = 0
        right = len(nums) - 1

        while left <= right:

            middle = (left + right) // 2

            if nums[middle] == target:
                first = middle
                right = middle - 1

            elif nums[middle] < target:
                left = middle + 1
            
            else:
                right = middle - 1

        last = -1
        left = 0
        right = len(nums) - 1

        while left <= right:

            middle = (left + right) // 2

            if nums[middle] == target:
                last = middle
                left = middle + 1

            elif nums[middle] < target:
                left = middle + 1

            else:
                right = middle - 1
                
        return [first, last]
