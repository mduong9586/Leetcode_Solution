class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        h = len(nums) - 1
            
        while l < h:
            m = (l + h) / 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                h = m-1
            else:
                l = m+1
        if nums[h] == target:
            return h
        return -1
