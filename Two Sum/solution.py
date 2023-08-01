class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            for j in range(0, nums - 1):
                if i + j == target:
                    return nums[i], nums[j]
